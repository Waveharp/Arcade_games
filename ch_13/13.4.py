class Cat():
	name = ""
	color = ""
	weight = 0

	def meow(self):
		print("Meow.")

Harley = Cat()
Harley.name = "Harley"
Harley.color = "orange"
Harley.weight = 10

Harley.meow()

class Monster():
	name = ""
	health = 0

	def decreaseHealth(self, amount):
		self.health = self.health - amount
		if self.health >= 0:
			print("The Monster has died.")
		else:
			print("The Monster is still alive.")

Orc = Monster()
Orc.name = "Ork"
Orc.health = 15

Orc.decreaseHealth(Orc, 10)

print(Orc.health)