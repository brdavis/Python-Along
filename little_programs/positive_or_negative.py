# This program checks if a number is positive or negative

# This function determines if its argument is positive or negative
def pos_or_neg(x):
	if x > 0:
		print "The number you entered is positive"
	elif x < 0: 
		print "The number you entered is negative"
	else:
		print "Zero is a special case"

# Directions and gather user input
number = int(raw_input("Enter a number to find out if it is positive or negative: "))

# Calculate and print results
pos_or_neg(number)
