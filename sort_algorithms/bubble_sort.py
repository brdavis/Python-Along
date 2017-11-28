# This program performs bubble sort

def bubble_sort(given_list):
	# outter loop for each pass
	for j in range(len(given_list)-1, 0, -1):
		# inner loop for iterating through elements in each pass
		for i in range(j):
			# test the two numbers
			if given_list[i] > given_list[i+1]:
			# swap numbers
				temp = given_list[i]
				given_list[i] = given_list[i+1]
				given_list[i+1] = temp

# set list variable
unsorted_list = [2, 5, 7, 1, 3]

# perform bubble sort on the unsorted list and print as a  sorted list
bubble_sort(unsorted_list)
print(unsorted_list) # (now sorted)
