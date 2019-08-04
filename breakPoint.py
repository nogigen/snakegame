class breakPoint(object):
	def __init__(self, x , y , direction):
		self.__x = x
		self.__y = y
		self.__direction = direction

	def getX(self):
		return self.__x

	def getY(self):
		return self.__y

	def getDirection(self):
		return self.__direction