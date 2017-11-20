# This program checks if a number is a prime number

# This function checks if its argument is a prime number
def check_prime(x):
	if x < 2:
		return True

	for i in range(2,x):
		if (x%i == 0):
			return False
	return True

# Directions and gather user input
number = int(raw_input("Enter a number to determine if it is prime: "))

# Calculate if number is prime
is_prime = check_prime(number)

# Print results
if is_prime:
	print "The number you entered is prime"
else:
	print "The number you entered is not prime"






