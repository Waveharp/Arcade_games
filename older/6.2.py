def ex1():
	for i in range(10):
		print "*",

def ex2():
	for i in range(10):
		print "*",
	print
	for i in range(5):
		print "*",
	print
	for i in range(20):
		print "*",
	print

def ex3():
	for i in range(10):
		for i in range(10):
			print "*",
		print

def ex4():
	for row in range(10):
		for column in range(5):
			print "*",
		print

def ex5():
	for row in range(5):
		for column in range(20):
			print "*",
		print

def ex6():
	for row in range(10):
		for i in range(10):
			print i,
		print

def ex7():
	for row in range(10):
		for column in range(10):
			print row,
		print

def ex8():
	for row in range(11):
		for i in range(row):
			print i,
		print

def ex9():
	for row in range(10):
		for i in range(row):
			print " ",
		for i in range(10-row):
			print i,
		print

def ex10():
	for i in range(1,10):
		for j in range(1,10):
			if i*j < 10:
				print "",
			print i*j,
		print

def ex11():
	for i in range(1,10):
		for j in range(10-i):
			print "",
		for j in range(1,i+1):
			print j,
		for j in range(i-1,0,-1):
			print j,
		print


ex11()