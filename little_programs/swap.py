# This program swaps two variables using a third, temporary variabel

# Collect values for two variables
x = int(raw_input("Enter a number for x: "))
y = int(raw_input("Enter a number for y: "))

# Print values before swap
print "Before swap x = %d and y = %d" % (x, y)

# Perform swap
temp = x
x = y
y = temp

# Print results after swap
print "After swap x = %d and y = %d" % (x, y)
