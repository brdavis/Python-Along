# In fibonacci series the sum of two elements defines the next

def fibonacci_series_v1():

	#directions and gather user input
	stopping_threshold = int(raw_input("How many numbers from the fibonacci series would you like to see printed?"))
	
	#initialize variables a and b, and counter i
	a = 1
	b = 1
	i = 1
	
	#calculated and print result
	while i <= stopping_threshold:
		print b
		temp = a
		a = b
		b = b + temp
		i = i + 1

#call program
fibonacci_series_v1()
