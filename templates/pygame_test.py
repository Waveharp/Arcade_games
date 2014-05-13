import pygame
pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# define pi (or just import it)
pi = 3.141592653

# opening a window and setting size
size = (700, 500)
screen = pygame.display.set_mode(size)

# set a window title
pygame.display.set_caption("Game of Badassdom")

# loop until user exits
done = False

# manages how fast screen updates
clock = pygame.time.Clock()

# main loop
while not done:
	# all event processing goes below this line
	for event in pygame.event.get(): # user did something
		if event.type == pygame.QUIT: # if user clicked close
			done = True
	# done with event processing

	# first clear the screen to white
	screen.fill(WHITE)

	# drawing a line from 0,0 to 100,100 with a width of 5 px
	pygame.draw.line(screen, GREEN, [0,0], [100, 100], 5)

	# drawing a series of lines
	for y_offset in range(0,100,10):
		pygame.draw.line(screen, RED, [0,10+y_offset], [100,110+y_offset], 5)

	# draw a rectangle
	pygame.draw.rect(screen,BLACK,[20,20,250,100],2)

	# draw an ellipse
	pygame.draw.ellipse(screen,BLACK,[20,20,250,100],2)

	# draw an arc as part of an ellipse
	pygame.draw.arc(screen,GREEN,[100,100,250,200], pi/2, pi, 2)

	# draw a polygon
	pygame.draw.polygon(screen,BLACK,[[100,100],[0,200],[200,200]],5)

	# drawing text
	# font - default, 25 pt
	font = pygame.font.Font(None, 25)
	# render the text. "True" means anti-aliased
	text = font.render("My text",True,BLACK)
	# this line renders text to screen
	screen.blit(text, [250,250])

	# update screen with what's been drawn
	pygame.display.flip()

	# limit fps
	clock.tick(60)

pygame.quit()