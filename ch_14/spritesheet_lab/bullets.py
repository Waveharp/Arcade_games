import pygame
import random
import constants
import player

class Bullet(pygame.sprite.Sprite):
	""" This class represents the bullet. """
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("fireball.png")
		self.rect = self.image.get_rect()

	def update(self):
		""" Move the bullet. """
		if player.Player.direction == "R":
			self.rect.x += 3
		elif player.Player.direction == "L":
			self.rect.x -= 3