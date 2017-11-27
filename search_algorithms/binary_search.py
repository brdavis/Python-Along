# This program performs a binary search

def binary_search(given_list, target):
	first_element = 0
	last_element = len(given_list) -1

	while first_element <= last_element:
		midpoint_element = (first_element + last_element)/ 2
		if given_list[midpoint_element] == target:
			return True
		else:
			if target < given_list[midpoint_element]:
				last_element = midpoint_element - 1
			else:
				first_element = midpoint_element + 1
	return False	

# Run binary search a print results
example_list = [1,3,4,5,7,10]
print(binary_search(example_list, 4)) #True
print(binary_search(example_list, 6)) #False
