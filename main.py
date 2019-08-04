import random
import pygame
from node import node
from snake import snake
from breakPoint import breakPoint

def snackPos(s, sizeBetween):
	nodes = s.getNodes()
	flag = True
	while flag:
		count = 0
		snackXRow = random.randint(0,19)
		snackYRow = random.randint(0,19)
		snackX = snackXRow * sizeBetween + (sizeBetween / 2)
		snackY = snackXRow * sizeBetween + (sizeBetween / 2)
		for node in nodes:
			if node.getX() == snackX and node.getY() == snackY:
				count += 1
		if count == 0:
			flag = False
	return (snackX, snackY)

# draw snack
def drawSnack(surface, posSnake):
	radius = 6
	pygame.draw.circle(surface, (255,192,203), (round(posSnake[0]),round(posSnake[1])), radius)
			

def snackEaten(snake, posSnake):
	nodes = snake.getNodes()
	count = 0
	for node in nodes:
		if node.getX() == posSnake[0] and node.getY() == posSnake[1]:
			count += 1

	if count == 0:
		return False

	return True

# drawing grid
def drawGrid(surface):
	global width
	global rows

	sizeBtwn = width // rows
	x = 0
	y = 0
	for i in range(rows - 1):
		x += sizeBtwn
		y += sizeBtwn

		pygame.draw.line(surface, (255,255,255), (x,0),(x,width))
		pygame.draw.line(surface, (255,255,255), (0,y),(width,y))

# draw everything in this
def redrawWindow(surface,snake, snackXandY):
	surface.fill((0,0,0))
	drawGrid(surface)
	drawSnack(surface, snackXandY)
	snake.draw(surface)
	pygame.display.update()

# main loop
def main():
	global width
	global rows
	width = 500
	rows = 20
	sizeBtwn = width // rows	
	win = pygame.display.set_mode( (width, width) )
	s = snake(sizeBtwn)
	snackXandY = snackPos(s, sizeBtwn)
	flag = True
	clock = pygame.time.Clock()

	while flag:
		clock.tick(15) # 15 frames in 1 second

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				flag = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					s.addBreakPoint("WEST")
				elif event.key == pygame.K_RIGHT:
					s.addBreakPoint("EAST")
				elif event.key == pygame.K_UP:
					s.addBreakPoint("NORTH")
				elif event.key == pygame.K_DOWN:
					s.addBreakPoint("SOUTH")

		if snackEaten(s, snackXandY):
			s.addNode()
			snackXandY = snackPos(s, sizeBtwn)

		redrawWindow(win,s, snackXandY)
		s.move()

# main function
main()
pygame.quit()