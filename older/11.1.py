"""
	Show how to use a sprite backed by a graphic.
	
"""

import pygame

# use of the main function in Ch. 9

# defining colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# draw a snowman
def draw_snowman(screen, x, y):
	# draw a circle for head
	pygame.draw.ellipse(screen, WHITE,[35+x, 0+y, 25, 25])
	# draw middle
	pygame.draw.ellipse(screen, WHITE,[23+x, 20+y, 50, 50])
	# draw bottom circle
	pygame.draw.ellipse(screen, WHITE,[0+x, 65+y, 100, 100])
	
# draw a stick figure
def draw_stickfigure(screen, x, y):
	# head 
	pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)
	
	# legs
	pygame.draw.line(screen, BLACK, [5+x,17+y], [10+x,27+y], 2)
	pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)
	
	# body
	pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)
	
	# arms
	pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
	pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)

def main():
	""" Main function for the game. """
	pygame.init()
	
	# set width, height of screen
	size = [700, 500]
	screen = pygame.display.set_mode(size)
	
	pygame.display.set_caption("Game of Badassdom")
	
	# loop until user clicks close button
	done = False
	
	clock = pygame.time.Clock()
	
	# Hide the mouse cursor
	pygame.mouse.set_visible(False)
	
	# speed in pixels per frame
	x_speed = 0
	y_speed = 0
	
	# current position
	x_coord = 10
	y_coord = 10
	
	# count joysticks
	joystick_count = pygame.joystick.get_count()
	if joystick_count == 0:
		# no joysticks!
		print("Error, I didn't find any joysticks.")
	else:
		# use joystick #0 and initialize it
		my_joystick = pygame.joystick.Joystick(0)
		my_joystick.init()
	
	# --- Main Program Loop ---
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			# user pressed a key down
			if event.type == pygame.KEYDOWN:
				# is it an arrow key? if yes, adjust speed
				if event.key == pygame.K_LEFT:
					x_speed = -3
				if event.key == pygame.K_RIGHT:
					x_speed = 3
				if event.key == pygame.K_UP:
					y_speed = -3
				if event.key == pygame.K_DOWN:
					y_speed = 3
			
			# user let up on a key
			if event.type == pygame.KEYUP:
				# if it's an arrow key, reset vector to zero
				if event.key == pygame.K_LEFT:
					x_speed = 0
				if event.key == pygame.K_RIGHT:
					x_speed = 0
				if event.key == pygame.K_UP:
					y_speed = 0
				if event.key == pygame.K_DOWN:
					y_speed = 0
			
		# move object according to speed vector
		x_coord += x_speed
		y_coord += y_speed
		
		# prevent stickman from leaving screen - mostly
		if x_coord < 0:
			x_coord = 0
		if x_coord > 690:
			x_coord = 690
		if y_coord < 0:
			y_coord = 0
		if y_coord > 490:
			y_coord = 490
			
		pos = pygame.mouse.get_pos()
		x = pos[0]
		y = pos[1]	
		
		# joystick stuff
		if joystick_count != 0:
			# gets position of axis on controller
			# returns a number between -1.0 and 1.0
			horiz_axis_pos = my_joystick.get_axis(0)
			vert_axis_pos = my_joystick.get_axis(1)
			
			# move according to the axis. multiply to speed up movement
			# convert to an int because pixels can only be drawn at whole numbers
			x_coord = x_coord + int(horiz_axis_pos * 10)
			y_coord = y_coord + int(vert_axis_pos * 10)
			
		screen.fill(WHITE)
		
		draw_stickfigure(screen, x_coord, y_coord)
		
		pygame.display.flip()
		
		clock.tick(60)
		
	pygame.quit()
	
if __name__ == "__main__":
	main()
