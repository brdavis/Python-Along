# This program determines if a given number is odd or even

# This function determines if an argument is odd or even
def odd_or_even(x):
	if x%2 == 0:
		print "The number you entered is even"
	else:
		print "The number you entered is odd"

# Directions and gather user input
number = int(raw_input("Enter a number to determine if it is odd or even: "))

# Calculate and print results
odd_or_even(number)
