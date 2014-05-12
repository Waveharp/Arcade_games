import pygame
import random

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow Animation")

# loop until user clicks close button
done = False

# manage how fast screen updates
clock = pygame.time.Clock()

snow_list = []

for i in range(75):
	x = random.randrange(0, 700)
	y = random.randrange(0, 500)
	snow_list.append([x, y])

# main program loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	screen.fill(BLACK)
	for i in range(len(snow_list)):
		# draw the snowflake
		pygame.draw.circle(screen, WHITE, snow_list[i], 2)
		# move snowflake down one pixel
		snow_list[i][1] += 1
		
		# regenerates snow
		if snow_list[i][1] > 500:
			# reset it just above screen
			y = random.randrange(-50, -10)
			snow_list[i][1] = y
			# give it a new x position
			x = random.randrange(0, 400)
			snow_list[i][0] = x

		
	pygame.display.flip()
	
	clock.tick(20)
	
pygame.quit()
