"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
from my_classes import *
from goodblock_file import *
from badblock_file import *

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite."""

    # -- attributes
    # speed vector
    change_x = 0
    change_y = 0

    # -- methods
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(WHITE)
        # make top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        """find a new position for the player""" 
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x < 0:
            self.rect.x = 0
            bump_sound.play()
        if self.rect.x > 680:
            self.rect.x = 680
            bump_sound.play()
        if self.rect.y < 0:
            self.rect.y = 0
            bump_sound.play()
        if self.rect.y > 370:
            self.rect.y = 370
            bump_sound.play()

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()

bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = GoodBlock("green_ball.png")
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)
 
for i in range(50):
    block = BadBlock("basketball.png")

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    bad_block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Player(50, 50, "player.png")
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
good_block_sound = pygame.mixer.Sound("good_block.wav")
bad_block_sound = pygame.mixer.Sound("bad_block.wav")
bump_sound = pygame.mixer.Sound("bump.wav")

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        # set speed based on key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        # reset speed upon key release
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # this actually moves player block based on current speed
    player.update()

    all_sprites_list.update()

    # Clear the screen
    screen.fill(WHITE)
 
 
    # See if the player block has collided with any good blocks
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
 
    # check for bad block collisions
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, False)

    # Check the list of collisions.
    for block in good_blocks_hit_list:
        good_block_sound.play()
        score += 1

    for block in bad_blocks_hit_list:
        bad_block_sound.play()
        score -= 1
        block.reset_pos()

    # print score to screen
    font = pygame.font.Font(None, 25)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [250, 10])

    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()