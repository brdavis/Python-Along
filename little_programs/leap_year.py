# This program determines if a year is a leap year

# This function determines if its input is a leap year
def check_leap_year(year):
	if (year%400 == 0):
		print "It is a leap year"
	elif (year%100 == 0):
		print "It is not a leap year"
	elif (year%4 == 0):
		print "It is a leap year"
	else:
		print "It is not a leap year"

# Directions and gather user input
year = int(raw_input("Enter a year to determine if it is a leap year: "))

# Calculate and print results
check_leap_year(year)
