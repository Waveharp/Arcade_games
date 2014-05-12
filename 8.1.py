import pygame

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

pygame.display.set_caption("Game of Badassdom")

# loop until user clicks close button
done = False

# manage how fast screen updates
clock = pygame.time.Clock()

# starting position of rectangle
rect_x = 50
rect_y = 50

# speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

# main program loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	screen.fill(BLACK)
	pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])
	pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
	rect_x += rect_change_x
	rect_y += rect_change_y
	# bounce the rectangle if needed
	if rect_y > 450 or rect_y < 0:
		rect_change_y = rect_change_y * -1
	if rect_x > 650 or rect_x < 0:
		rect_change_x = rect_change_x * -1
	
	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()
