# In fibonacci series the sum of two elements defines the next

def fibonacci_series_v2():

	#directions and gather user input
	stopping_threshold = int(raw_input("How many numbers from the fibonacci series would you like to see printed?"))
	
	#initialize variables a and b, and counter i
	a, b, i = 1, 1, 1
	
	#calculated and print result
	while i <= stopping_threshold:
		print b
		a, b = b, a+b
		i = i + 1

#call program
fibonacci_series_v2()
