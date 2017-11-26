# This program perform Sequential Search 

def sequential_search(given_list, target):
	target_found = False
	i = 0
	
	while i < len(given_list) and not target_found:
		if given_list[i] == target:
			target_found = True
		else:
			i = i + 1

	return target_found

# set list
example_list = [1, 2, 3, 5, 7, 8]

# perform sequential search and print results
print (sequential_search(example_list, 7)) # True
print (sequential_search(example_list, 4)) # False

