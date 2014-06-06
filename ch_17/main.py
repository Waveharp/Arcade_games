
"""
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (0, 0, 255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (255, 255)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False

width = 20
height = 20
margin = 5 

# text stuff
font = pygame.font.SysFont('Calibri', 25, True, False)
click_text = font.render("click", True, WHITE)

# create a grid of numbers
# create an empty list
grid = []
# loop for each row
for row in range(10):
    # for each row, create a list that will represent an entire row
    grid.append([])
    # loop for each column
    for column in range(10):
        # add the number 0 to current row
        grid[row].append(0)

# you could also do this using list comp:
# grid = [[0 for x in range(10)] for y in range(10)]

# set row 1, column 5 to zero
grid[1][5] = 1

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # user clicks mouse, get position
            pos = pygame.mouse.get_pos()
            # change x/y screen coords to grid coords
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            # set that location to zero
            grid[row][column] = 1
            print("Click: ", pos, "Grid coords: ", row, ",", column)
 
    # --- Game logic should go here
 
    # --- Drawing code should go here

    # get mouse position
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    # convert mouse position to grid coordinates

 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command
    screen.fill(BLACK)
    for row in range(10):
        for column in range(10):
            color = BLUE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen, color,[(width+margin)*column+margin, 
                                            (height+margin)*row+margin, width, height])

    
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()