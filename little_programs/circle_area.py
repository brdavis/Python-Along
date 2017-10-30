import math

def circle_area(radius):
	area = math.pi * math.pow(radius, 2)
	return area

given_radius = int(raw_input("Enter the radius of the circle"))
print circle_area(given_radius)

	
