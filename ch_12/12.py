"""
	Chapter 12
	
"""

import pygame

# defining colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
	""" Main function for the game. """
	pygame.init()
	
	# set width, height of screen
	size = [800, 600]
	screen = pygame.display.set_mode(size)
	
	pygame.display.set_caption("Game of Badassdom")
	
	# loop until user clicks close button
	done = False
	
	clock = pygame.time.Clock()

	# load the background image
	background_image = pygame.image.load("infinite-connection.jpg").convert()

	# load laser sound
	click_sound = pygame.mixer.Sound("laser5.ogg")

	# --- Main Program Loop ---
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				click_sound.play()
				
		screen.fill(WHITE)
		
		# draw the background
		screen.blit(background_image, [0, 0])

		# draw the player's ship
		player_image = pygame.image.load("player.png").convert()
		# set the color black to transparent
		player_image.set_colorkey(BLACK)

		# get current mouse position. returns pos
		# as a list of two numbers
		player_position = pygame.mouse.get_pos()
		x = player_position[0]
		y = player_position[1]

		# copy image to screen
		screen.blit(player_image, [x, y])
		
		pygame.display.flip()
		
		clock.tick(20)
		
	pygame.quit()
	
if __name__ == "__main__":
	main()
