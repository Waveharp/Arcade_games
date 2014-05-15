import pygame

# class example
class Character():
	name = "Link"
	sex = "Male"
	max_hit_points = 50
	current_hit_points = 50
	max_speed = 10
	armor_amount = 8

# example 2
class Address():
	name = "Tyler Durden"
	line1 = "1537 Paper Street"
	line2 = ""
	city = "Bradford"
	state = "Deleware"
	zip = "19808"

# create an instance of the address class 
# create an address
homeAddress = Address()

# set fields in the address
homeAddress.name = "Tyler Durden"
homeAddress.line1 = "1537 Paper Street"
homeAddress.city = "Bradford"
homeAddress.state = "Deleware"
homeAddress.zip = "19808"

# create another address
vacationHomeAddress = Address()

# set fields in address 2
vacationHomeAddress.name = "Jack"
vacationHomeAddress.line1 = "1122 Main Street"
vacationHomeAddress.line2 = ""
vacationHomeAddress.city = "Panama City Beach"
vacationHomeAddress.state = "FL"
vacationHomeAddress.zip = "32407"

print("The client's main home is in " + homeAddress.city)
print("His vacation home is in " + vacationHomeAddress.city)

# print an address to the screen
def printAddress(address):
	print(address.name)
	# if there is a line1, print it 
	if(len(address.line1) > 0):
		print(address.line1)
	# if there's a line 2...
	if(len(address.line2) > 0):
		print(address.line2)
	print(address.city + ", "+address.state+" "+address.zip)

printAddress(homeAddress)
print()
printAddress(vacationHomeAddress)