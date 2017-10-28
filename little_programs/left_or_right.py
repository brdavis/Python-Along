def left_or_right():
	print "Pick if you would like to go to the left or the right"
	answer = raw_input("Type left or right and hit 'Enter'").lower()
	if answer == "left" or answer == "l":
		print "You picked left"
	elif answer == "right" or answer == "r":
		print "You picked right"
	else:
		print "You are directionless"
		left_or_right()
left_or_right()
