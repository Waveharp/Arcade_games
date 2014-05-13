import pygame
import random

# use of the main function in Ch. 9

# defining colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle():
	x = 0
	y = 0
	width = 0
	height = 0
	change_x = 0
	change_y = 0
	color = [0, 0, 0]

	def draw(self, screen):
		pygame.draw.rect(screen, self.color,[self.x, self.y, self.width, self.height])

	def move(self):
		self.x = self.x + self.change_x
		self.y = self.y + self.change_y
		if self.x < 0 or self.x > 700:
			self.change_x = self.change_x * -1
		if self.y < 0 or self.y > 500:
			self.change_y = self.change_y * -1

class Ellipse(Rectangle):
	def draw(self, screen):
		pygame.draw.ellipse(screen, self.color,[self.x, self.y, self.width, self.height])

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

	myList = []
	for i in range(100):
		myObject = Rectangle()
		myObject.change_x = random.randint(-3, 3)
		myObject.change_y = random.randint(-3, 3)
		myObject.x = random.randint(0, 700)
		myObject.y = random.randint(0, 500)
		myObject.height = random.randint(20, 70)
		myObject.width = random.randint(20, 70)
		myObject.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
		myList.append(myObject)
	
	for i in range(100):
		myObject = Ellipse()
		myObject.change_x = random.randint(-3, 3)
		myObject.change_y = random.randint(-3, 3)
		myObject.x = random.randint(0, 700)
		myObject.y = random.randint(0, 500)
		myObject.height = random.randint(20, 70)
		myObject.width = random.randint(20, 70)
		myObject.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
		myList.append(myObject)

	# --- Main Program Loop ---
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
		screen.fill(BLACK)
		
		for item in myList:
			item.draw(screen)
			item.move()

		pygame.display.flip()
		
		clock.tick(20)
		
	pygame.quit()
	
if __name__ == "__main__":
	main()
