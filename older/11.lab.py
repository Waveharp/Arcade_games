"""
	basic game template using main()
	
"""

import pygame

# use of the main function in Ch. 9

# defining colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_robot(screen, x, y):
	# draw the head
	pygame.draw.rect(screen, BLACK, [x, y, 35, 40]

def main():
	""" Main function for the game. """
	pygame.init()
	
	# set width, height of screen
	size = [700, 500]
	screen = pygame.display.set_mode(size)
	
	pygame.display.set_caption("Game of Badassdom")
	
	# loop until user clicks close button
	done = False
	
	pygame.mouse.set_visible(False)
	
	clock = pygame.time.Clock()
	
	# --- Main Program Loop ---
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
		screen.fill(WHITE)
		
		draw_robot(screen, x, y)
		
		pygame.display.flip()
		
		clock.tick(20)
		
	pygame.quit()
	
if __name__ == "__main__":
	main()
