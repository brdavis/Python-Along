# This program swaps two variables using a third, temporary, variable

# set the two variables
x = 2
y = 3

# print before swap
print "Before swapping x = %d and y = %d" % (x, y)

# perform swap
temp = x
x = y
y = temp

# print after swap
print "After swapping x = %d and y = %d" % (x, y)
