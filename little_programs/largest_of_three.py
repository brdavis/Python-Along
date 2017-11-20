# This program determines the largest of 3 numbers

# This function determines the largest of three numbers
def find_largest(x, y, z):
	if (x >= y) and (x >= z):
		return x;
	elif (y >= x) and (y >= z):
		return y;
	else:
		return z;

# Directions and gather user input
print "\nThis program will tell you the largest of three numbers"
n1 = int(raw_input("Enter the first number: "))
n2 = int(raw_input("Enter the second number: "))
n3 = int(raw_input("Enter the third number: "))

# Calculate and print the result
largest = find_largest(n1, n2, n3)
print "The largest number is %d" % (largest) 
