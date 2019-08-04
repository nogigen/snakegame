import pygame
from breakPoint import breakPoint

class node(object):
	__width = 500
	__height = 500
	__radius = 6
	def __init__(self, x , y , headDirection, sizeBetween, isHead):
		self.__sizeBetween = sizeBetween 
		self.__isHead = isHead # boolean
		self.__breakPoints = []
		self.setXandY(x,y,headDirection)



	def setXandY(self, x , y , headDirection):
		if headDirection == "WEST":
			self.__x = x + self.__sizeBetween
			self.__y = y
		elif headDirection == "EAST":
			self.__x = x - self.__sizeBetween
			self.__y = y
		elif headDirection == "SOUTH":
			self.__x = x
			self.__y = y - self.__sizeBetween
		else:
			self.__x = x
			self.__y = y + self.__sizeBetween

	# move node -> update its x and y
	def move(self, headDirection):
		self.checkBreakPoint()	


		if len(self.__breakPoints) > 0:
			if self.__breakPoints[0].getDirection() == "EAST":
				self.__x = self.__x + self.__sizeBetween
			elif self.__breakPoints[0].getDirection() == "WEST":
				self.__x = self.__x - self.__sizeBetween
			elif self.__breakPoints[0].getDirection() == "NORTH":
				self.__y = self.__y - self.__sizeBetween
			else:
				self.__y = self.__y + self.__sizeBetween
		else:
			if headDirection == "EAST":
				self.__x = self.__x + self.__sizeBetween
			elif headDirection == "WEST":
				self.__x = self.__x - self.__sizeBetween
			elif headDirection == "NORTH":
				self.__y = self.__y - self.__sizeBetween
			else:
				self.__y = self.__y + self.__sizeBetween

		if self.__x < 0:
			self.__x = self.__x + self.__width
		elif self.__x > self.__width:
			self.__x = self.__x - self.__width

		if self.__y < 0:
			self.__y = self.__y + self.__height
		elif self.__y > self.__height:
			self.__y = self.__y - self.__height



	# draw the node.
	def draw(self,surface):
		if self.__isHead:
			pygame.draw.circle(surface, (140,132,222), (round(self.__x), round(self.__y)), self.__radius)

		else:
			pygame.draw.circle(surface, (255,0,0), (round(self.__x), round(self.__y)), self.__radius)
			

	def checkBreakPoint(self):
			
		if len(self.__breakPoints) > 0:						
			if self.__x == self.__breakPoints[0].getX() and self.__y == self.__breakPoints[0].getY():
				self.__breakPoints.pop(0)

			

	def addBreakPoint(self, breakPoint):
		if not self.__isHead:
			self.__breakPoints.append(breakPoint)

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def getDirection(self, headDirection):
		if len(self.__breakPoints) > 0:
			return self.__breakPoints[0].getDirection()
		return headDirection

	


	