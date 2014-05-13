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

b = Boat()

b.dock()
b.undock()
b.undock()
b.dock()
b.dock()