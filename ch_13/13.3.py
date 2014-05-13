import pygame

class Dog():
	age = 0
	name = ""
	weight = 0

	def bark(self):
		print("Woof says", self.name)

class Ball():
	# --- Class Attributes ---
	# Ball position
	x = 0
	y = 0

	# Ball's vector
	change_x = 0
	change_y = 0

	# Ball size
	size = 10

	# ball color
	color = [255, 255, 255]

	# --- Class Methods ---
	def move(self):
		self.x += self.change_x
		self.y += self.change_y

	def draw(self, screen):
		pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

# create an instance of Ball
theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255, 0, 0]

# to move the ball (this would go in main loop)
theBall.move()
theBall.draw(screen)

myDog = Dog()

myDog.name = "Spot"
myDog.weight = 30
myDog.age = 3

myDog.bark()

