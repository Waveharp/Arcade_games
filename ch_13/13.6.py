# inheritance! 
class Boat():
	tonnage = 0
	name = ""
	isDocked = True

	def dock(self):
		if self.isDocked:
			print("You are already docked.")
		else:
			self.isDocked = True
			print("Docking")

	def undock(self):
		if not self.isDocked:
			print("You aren't docked.")
		else:
			self.isDocked = False
			print("Undocking.")

class Submarine(Boat):
	def submerge(self):
		print("Submerge!")

class Person():
	name = ""

	# you can inherit constructors...
	def __init__(self):
		print("Person created.")

class Employee(Person):
	job_title = ""

	# and override them
	def __init__(self):
		print("Employee created.")

class Customer(Person):
	email = ""

	# or specifically call the parent's method
	def __init__(self):
		Person.__init__(self)
		print("Customer created.")

b = Boat()

b.dock()
b.undock()
b.undock()
b.dock()
b.dock()

johnSmith = Person()
johnSmith.name = "John Smith"

janeEmployee = Employee()
janeEmployee.name = "Jane Employee"
janeEmployee.job_title = "Web Dev"

bobCustomer = Customer()
bobCustomer.name = "Bob Customer"
bobCustomer.email = "send_me@email.com"
