import math
try:
	from Queue import PriorityQueue as pq
except: 
	from queue import PriorityQueue as pq

def init(door_r, arm_r, robo_dim, arena, desc):
	node.door_r = door_r
	node.arm_r = arm_r
	node.Width = robo_dim[0]
	node.Len = robo_dim[1]
	node.arena_W = arena[0]
	node.arena_L = arena[1]
	node.dx = desc[0]
	node.dy = desc[1]

class node:

	# default values of the parameters
	door_r = 1 			# radiusof the door
	arm_r = 1 			# radius of arm's workspace
	# dimensions of robo
	Width = 0.4  	# along the x
	Len = 0.4 		# along the y

	# dimensions of the arena
	arena_W = 2.4		# along x
	arena_L = 2.4
	dx = Width/4
	dy = Len/4


	def __init__(self,x,y,theta,d,h,v,gcost,parentkey):
		self.x = x
		self.y = y
		self.theta = theta
		self.d = d 		# 0: closed, 1: open 2: overlap, door interval
		self.h = h 		# 0: Outside, 1: inside	, side of the door in contact
		self.v = v 		# 0: Arm , 1: base , part of robot in contact
		self.parentkey = parentkey 
		self.gcost = gcost
		self.hcost = self.getHcost()

	def getSuccs(self):
		# transitions in SECOND primitives
		# (h,v) ==(0,1) -> NOT possible, holding door by base from outside
		# (1,1) -> special case, (1,0)-> final/goal case: arm from inside, 
		# (0,0)-> initial state

		# the only transition possible when in contact with base from inside
		#transition from base to arm 
		if (self.h == 1 and self.v == 1 and self.d == 1):
			vnew = 0
			tempNode = node(self.x,self.y,self.theta,self.d,self.h,vnew,\
					self.gcost,self.gethashKey())
			action = 5
			tempNode.gcost += tempNode.getTCost(action)
			return [tempNode]

		#list to be returned
		succs = []
		#transition from arm to base and outside to inside
		# (d,h,v) = (1,0,0) -> (1,1,1)
		if (self.h == 0 and self.d == 1 and self.v == 0):
			if math.hypot(self.x,self.y) > node.door_r - node.arm_r/2:
				hnew = 1
				vnew = 1
				tempNode = node(self.x,self.y,self.theta,self.d,hnew,vnew,\
					self.gcost,self.gethashKey())
				action1 = 4
				action2 = 5
				tempNode.gcost += tempNode.getTCost(action1) #+ tempNode.getTCost(action2)
				if tempNode.stateIsvalid():
					succs += [tempNode]
		
		# transition in base footprint
		dx = node.dx
		dy = node.dy
		dtheta = 10

		Posx = []
		Posx += [[self.x + dx,self.y,self.theta]]
		Posx += [[self.x - dx,self.y,self.theta]]

		Posy = []
		#Posy = Posx
		Posy += [[self.x,self.y + dy,self.theta]]
		Posy += [[self.x ,self.y - dy,self.theta]]
		PosT = []
		# creating the nodes and cost of nodes depending on door interval
		succs = []

		for item in Posx:
			succs += self.variants(item, 0)
		for item in Posy:
			succs += self.variants(item, 1)
		# can do the same for change in theta
		
		# shifting between v values and h vales
		tempNode = self
		if self.d == 1:
			# transfering from to base to arm
			if self.h == 0 and self.v == 0:
				tempNode.h = 1
				tempNode.v = 1
				action = 5
				tempNode.gcost += tempNode.getTCost(action)
				if tempNode.stateIsvalid():
					succs += [tempNode]
				else: 
					print 'failure'
				
			# transfering from base to arm
			elif self.h == 1 and self.v ==1:
				tempNode.v = 0
				action = 5
				tempNode.gcost += tempNode.getTCost(action)
				if tempNode.stateIsvalid():
					succs += [tempNode]
				else:
					print 'failure'

		return succs

# Motion primitive / variants for each change in pose
	def variants(self,item,action):
		succs = []
		tempNode = node(item[0],item[1],item[2],self.d,self.h,self.v,\
					self.gcost,self.gethashKey())
		tempNode2 = tempNode

		if tempNode.outDoorsweep():		# if it could be fully open
			
			if self.d == 2:				# if it already could be fully open
				action = 0
				tempNode.gcost += tempNode.getTCost(action)
				if tempNode.stateIsvalid():
					succs += [tempNode]
			if self.d == 0 : 			#if it was in closed interval
				dnew = 2
				action = 0
				tempNode.gcost += tempNode.getTCost(action)
				tempNode.d = dnew
				if tempNode.stateIsvalid():
					succs += [tempNode]
			if self.d == 1 and self.v == 0:			# if it was in open interval, held by arm
				dnew = 2
				action = 0
				tempNode.gcost += tempNode.getTCost(action)
				tempNode.d = dnew
				if tempNode.stateIsvalid():
					succs += [tempNode]
			#printNode(tempNode)

		else :		#if door cannot be fully open now
			if self.d == 2 :		# if it was fully openable in past
				# checking if it could be in open interval now 
				# NOTE: for door pulling case
				dnew = 1
				action = 0
				tempNode.d = dnew
				tempNode.gcost += tempNode.getTCost(action)
				if tempNode.stateIsvalid():
					succs += [tempNode]
			else : 		# let the door interval remain the same
				action = 0
				tempNode.gcost += tempNode.getTCost(action)
				if tempNode.stateIsvalid():
					succs += [tempNode]
		

		return succs


	def getHcost(self):
		rlen =  node.door_r
		posR = math.hypot(self.x, self.y)
		cost1 = max(0 , posR - rlen)
		
		angleRange = self.getFeasibleAngle()
		angleRange = angleRange[1] - angleRange[0]
		angleRem = 1.57 - angleRange
		cost2 = 0.1*angleRem
		
		return cost1 + cost2

	def gethashKey(self):
		haskey = self.x*100000 + self.y*10000 + self.theta*1000 + self.d*100 \
				+ self.h*10 + self.v
		return int(haskey)

	def getTCost(self, action):		# Cost of the transition
		cost = 0
		# 0: x , 1: y, 2:theta 3:d, 4:h, 5:v
		if action ==0:
			cost += 3
		elif action == 1:
			cost += 1
		elif action == 2:
			cost += 1
		elif action == 3:
			cost += 3
		elif action == 4:
			cost += 1
		elif action == 5:
			cost += 1

		return cost
	def getFeasibleAngle(self):
		if self.d == 0:
			roboAngle = round(math.atan2((self.y + node.Len),self.x)*100)/100	# accounting for robo size
			return [0, roboAngle]
		elif self.d == 1:
			roboAngle = round(math.atan2((self.y),(self.x + node.Width))*100)/100	# accounting for robo size
			return [roboAngle,1.57]
		else:
			return [0,1.57]

	def outDoorsweep(self):
		# true if d = 2 is possible
		if self.y >= 0:
			if self.d == 2 or self.d == 1:
				return True
		if math.hypot(self.x + node.Width/2, self.y  + node.Len/2) < node.door_r:
			return False
		# if self.x+ self.y + node.door_r > 0: 		# approximation of single line
		# 	return False
		# elif (self.x +node.Width/2  > -1*node.door_r - node.arm_r or \
		# 		self.y + node.Len/2 > -1*node.door_r - node.arm_r) :
		# 	return False 
		else:
			return True

	def stateIsvalid(self):
		#checking for arena constraints
		if (self.x < -1*node.door_r and self.y + node.Len/2 >0):
			# print 'barging into the wall', self.x, self.y
			return False
		if (self.x + node.Width/2 > 0 or self.x - node.Width/2 < -1*node.arena_W):
			# print 'barging into the wall', self.x, self.y
			return False
		elif self.y - node.Len/2 < -1*node.arena_L:
			# print 'barging into the wall', self.x, self.y
			return False

		elif self.d == 2:
			if math.hypot(self.x, self.y) > (node.door_r + node.arm_r) :
				# if it is beyond the reach of the arm
				return False
		# checking if it goes through with arm still holding the knob
		if self.d == 1 and self.h == 0:
			if self.y + node.Len/2 >= 0:
				return False

		##########################
		elif self.d == 0:
			# if it is in closed interval
			# if it barging into the door
			if self.y +node.Len/2 >= 0 :
				return False
			angle = self.getFeasibleAngle()
			angle = angle[1]

			#kinematic constraints
			# checking the distance from knob
			if math.hypot(self.x + node.door_r*math.cos(angle), \
							self.y + node.door_r*math.sin(angle)) < node.arm_r:
				# too far from door knob
				return False
		elif self.d == 1:
			# if the door is on open interval
			angle = self.getFeasibleAngle()
			angle = angle[0]
			# if the door is being held from outside
			if self.h == 0:
				if math.hypot(self.x + node.door_r*math.cos(angle), \
							self.y + node.door_r*math.sin(angle)) <  node.arm_r/2 :
					return True
			# if the door is being held from inside
			# elif self.h == 1 :
			# 	if math.hypot(self.x + node.door_r*math.cos(angle), \
			# 				self.y + node.door_r*math.sin(angle)) < node.arm_r :
			# 		return False
		return True

def getSatefromKey(key):
	x = key//100000
	y = (key-x*100000)//10000
	theta = (key - x*100000 - y*10000)//1000
	d = (key - x*100000 - y*10000 - theta*1000)//100
	h = (key - x*100000 - y*10000 - theta*1000 - d*100)//10
	v = (key - x*100000 - y*10000 - theta*1000 - d*100 - h*10)
	return [x,y,theta,d,h,v]

def getCost(Node, Weight):
	return (Weight*Node.getHcost() + Node.gcost)
def printNode(Node):
	if Node.d == 0:
		dstring = 'door in close intv '
	elif Node.d == 1:
		dstring = 'door in open intv '
	else:
		dstring = 'fully open door '
	if Node.h ==0:
		hstring = 'holding outside'
	else :
		hstring = 'holding inside'
	if Node.v == 0:
		vstring = 'using Arm'
	else:
		vstring = 'using base'
	print Node.x, Node.y, dstring, hstring, vstring
	print Node.gethashKey()

	return 0

def astar(start,goal,weight):
	print 	node.door_r ,node.arm_r , node.Width , node.Len ,node.arena_W , node.arena_L 
	closelist = {}
	openlist = pq()
	openlist_f = {}
	gstart = 0
	parent_start = 0
	start_node = node(start[0],start[1],start[2],0,0,0,gstart,parent_start)
	openlist.put((getCost(start_node,weight),start_node))
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
			printNode(node2exp)
			print node2exp.getFeasibleAngle()
			print 'number of expansions'
			print len(closelist)
			print 'teh cost'
			print getCost(node2exp, weight)	
			return [node2exp,closelist]
		if node2exp.y >0 :
			print 'goal reached'
			printNode(node2exp)
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
			openlist.put((getCost(item,weight),item))
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
