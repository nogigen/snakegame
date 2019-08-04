import random
from node import node
from breakPoint import breakPoint

class snake(object):	
	def __init__(self,sizeBetween):
		self.__sizeBetween = sizeBetween		
		self.reset()
		n = node(self.__x, self.__y, self.__direction, self.__sizeBetween, True)
		self.__nodes = []
		self.__nodes.append(n)

	# random direction
	def initialDirection(self):
		randomRow = random.randint(0,19)
		randomCol = random.randint(0,19)
		self.__x = randomRow * self.__sizeBetween + (self.__sizeBetween / 2)
		self.__y = randomRow * self.__sizeBetween + (self.__sizeBetween / 2)

	# random x and y
	def initialPositions(self):
		randomNumber = random.randint(0,3)
		if randomNumber == 0:
			self.__direction = "WEST"
		elif randomNumber == 1:
			self.__direction = "EAST"
		elif randomNumber == 2:
			self.__direction = "NORTH"
		else :
			self.__direction = "SOUTH"

	# reset direction , x , y and nodes
	def reset(self):
		self.initialDirection()
		self.initialPositions()

	# move all the nodes
	def move(self):
		for node in self.__nodes:
			node.move(self.__direction)

	# draw all the nodes
	def draw(self, surface):
		for node in self.__nodes:
			node.draw(surface)

	# add a node.
	def addNode(self):
		lastNode = self.__nodes[len(self.__nodes) - 1]
		x = lastNode.getX()
		y = lastNode.getY()
		direction = lastNode.getDirection(self.__direction)		
		newNode = node(x, y, direction,self.__sizeBetween, False)
		self.__nodes.append(newNode)


	# add a break point to all of the nodes.
	# also updates the direction of head.
	def addBreakPoint(self, direction):		

		for node in self.__nodes:
			newBreakPoint = breakPoint(self.__nodes[0].getX(), self.__nodes[0].getY(), self.__direction)
			node.addBreakPoint(newBreakPoint)

		self.__direction = direction


	def getNodes(self):
		return self.__nodes