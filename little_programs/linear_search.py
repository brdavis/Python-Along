# This program performs linear search



# linear search function
def linear_search(array, target):
	for element in range(len(array)):
		if array[element] == target:
			return element
	return -1



# drives linear search

# set variables of array and target element
example_array = [1,2,3,4,5,6,7,8,9,10]
target = int(raw_input("What number are you searching for?: "))

# calculate position of target in array
index = linear_search(example_array, target)

# print results
if index >= 0:
	print "Your number is located in position %d of the array" % (index + 1)
else:
	print "Your number was not in the array"	
