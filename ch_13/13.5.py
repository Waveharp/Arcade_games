# example of a class with a constructor
class Dog():
	name = ""

	# constructor
	# called when creating an object of this type
	def __init__(self, newName):
		self.name = newName
		print("A new dog is born!")

# this creates the dog
myDog = Dog("Spot")

# print the name to verify that it is set
print(myDog.name)
