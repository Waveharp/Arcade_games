import pygame
from my_classes import *
import random

class GoodBlock(Block):
	def update(self):
		self.rect.x += random.randint(-3, 3)
		self.rect.y += random.randint(-3, 3)