import pygame
import random
from my_classes import *

class BadBlock(Block):
	def update(self):
		self.rect.y += 1
		if self.rect.y > 400:
			self.reset_pos()

	def reset_pos(self):
		self.rect.y = random.randrange(-300, -20)
		self.rect.x = random.randrange(0, 700)