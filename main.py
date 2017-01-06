import astar
import time
from Node import node
import  Node 
# dimensions of robo and door

Width = 0.25  			# along the x
Len = 0.25 				# along the y
door_r = 4*Width 			# radiusof the door
arm_r = 1*door_r 			# radius of arm's workspace
goal = [-0.5,0.5,0]
start = [-1*door_r,-4*Width/2 ,0]
w = 1					# weight for astar




# dimensions of the arena
arena_W = door_r + Width + arm_r		# along x
arena_L = door_r + Len + arm_r

# descritization
desc =[Width/4, Len/4] 

#A star initialization
astar.init(door_r, arm_r, [Width, Len], [arena_W, arena_L], desc)

starttime = time.time()		# timer

# here comes the A star !!!
out =  astar.astar(start, goal, w)

end = time.time()
print 'time taken was ', end - starttime
gridSize1 = arena_W/(desc[0])
gridSize2 = arena_L/(desc[1])
print gridSize1, gridSize2

# getting the tree
print "figuring out the tree"
node_list = out[1]
currNode = out[0]
tree = []
tree += [currNode]
while True:
	pkey = currNode.parentkey
	if pkey == 0:
		print "tree finished"
		break
	newnode = node_list[pkey]
	tree += [newnode]
	#astar.printNode(newnode)
	currNode = newnode

print 'size of the path is'
print len(tree)

# writing the tree to a file
filename = 'tree2.txt'
fileobj = open(filename, 'w')

strtree = []
for item in reversed(tree):
	Node.printNode(item)
	oneline = []
	oneline += [str(item.x)]
	oneline += [str(item.y)]
	oneline += [str(item.d)]
	oneline += [str(item.h)]
	oneline += [str(item.v)]
	strtree += [oneline]
for item in strtree:
	print>>fileobj, item[0], item[1],item[2],item[3],item[4]
filename = 'prop.txt'
fileobj = open(filename,'w')
print>>fileobj,start[0],start[1], Width, Len, arm_r, arena_W, arena_L, door_r