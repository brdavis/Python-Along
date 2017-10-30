#	calculates the area of a square

# calculates area
def square_area(side):
	area = side * side
	return area

# gather input
given_side = int(raw_input("Enter the length of the side of the square"))

# call function and print result
result = square_area(given_side)
print "The area of your square is %d" % (result)
	
