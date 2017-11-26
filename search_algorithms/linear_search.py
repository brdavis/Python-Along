# This program performs linear seach (also known as sequential search)
# This implementation utilizes a 'For' loop as opposed to a 'While' loop

def linear_search(given_list, target):
	for i in range(len(given_list)):
		if given_list[i] == target:
			return True
	return False

# Run linear search and print results
example_list = [1,3,5,7]
print (linear_search(example_list, 3)) # True
print (linear_search(example_list, 8)) # Flase
