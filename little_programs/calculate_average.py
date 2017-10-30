# calculates the average of a given array

def calculate_average():
	#variables
	numbers = [1, 2, 3, 4, 5]
	total = 0

	#calculate average
	for i in range(0, len(numbers)):
		total = total + numbers[i]
	average = total/len(numbers)
	
	#return result
	return average

# call and print result
print calculate_average()

