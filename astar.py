try:
	from Queue import PriorityQueue as pq
except: 
	from queue import PriorityQueue as pq
from Node import node
import Node 


def init(door_r, arm_r, robo_dim, arena, desc):
	node.door_r = door_r
	node.arm_r = arm_r
	node.Width = robo_dim[0]
	node.Len = robo_dim[1]
	node.arena_W = arena[0]
	node.arena_L = arena[1]
	node.dx = desc[0]
	node.dy = desc[1]
def astar(start,goal,weight):
	print 	node.door_r ,node.arm_r , node.Width , node.Len ,node.arena_W , node.arena_L 
	closelist = {}
	openlist = pq()
	openlist_f = {}
	gstart = 0
	parent_start = 0
	start_node = node(start[0],start[1],start[2],0,0,0,gstart,parent_start)
	openlist.put((Node.getCost(start_node,weight),start_node))
	openlist_f[start_node.gethashKey()] = start_node
	while (openlist.qsize()>0):
		# print 'size of open list'
		# print openlist.qsize()
		# getting the node to expand 
		LCNode = openlist.get()			# least cost node
		node2exp = LCNode[1]
		# print 'the hcost from different calls'
		# print node2exp.hcost
		# print node2exp.getHcost()
		#print 'the node expand'
		#printNode(node2exp)
		#checking if the node2exp is the goal
		if node2exp.getHcost() == 0.00 :
			print 'goal reached via hcost'
			Node.printNode(node2exp)
			print node2exp.getFeasibleAngle()
			print 'number of expansions'
			print len(closelist)
			print 'teh cost'
			print Node.getCost(node2exp, weight)	
			return [node2exp,closelist]
		if node2exp.y >0 :
			print 'goal reached'
			Node.printNode(node2exp)
			return [node2exp,closelist]

		#expanding the node
		succs = node2exp.getSuccs()
		# print 'number of succs'
		# print len(succs)
		for item in succs:
			if item.gethashKey() in closelist:
				# print 'duplicate ', item.gethashKey() , ' is the key'
				continue
			if item.gethashKey() in openlist_f:
				# print 'duplicate in open list'
				continue
			# printNode(item)
			openlist.put((Node.getCost(item,weight),item))
			openlist_f[item.gethashKey()] = item

		# moving the expanded node to close list, and removing from open list dict
		closelist[node2exp.gethashKey()] = node2exp
		#del openlist_f[node2exp.gethashKey()]

	return 0


#  the main function
if __name__ == '__main__':
	import sys
	startx = float(sys.argv[1])
	starty = float(sys.argv[2])
	startTheta = float(sys.argv[3])
	goalx = float(sys.argv[4])
	goaly = float(sys.argv[5])
	goalTheta = float(sys.argv[6])
	w = float(sys.argv[7])
	out =  astar([startx, starty, startTheta], [goalx, goaly, goalTheta], w)
	if out == 0 :
		print 'failure'
	else:
		print 'success'
