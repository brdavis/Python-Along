#	Calculates cost of a vacation

# price of hotel
def hotel_budget(nights):
	return 150 * nights

# food budget
def food_budget(days):
	return 40 * days
	
# price of plane ticket
def plane_tickets(city):
	if city == "Seattle":
		return 120
	elif city == "New York":
		return 450
	elif city == "Los Angeles":
  		return 375
	else:
		return 0

# price of a rental car  
def rental_car_cost(days):
	total = days * 40
	if (days >= 7):
		return total - 50
	elif(days >= 3):
		return total - 20
	else:
		return total

# total cost of a trip
def trip_cost(city, days, spending_money):
	return hotel_budget(days) + food_budget(days) + plane_tickets(city) + rental_car_cost(days) + spending_money

# collect user input
city = raw_input("City (Seattle, New York, or Los Angeles): ")
days = int(raw_input("Number of days: "))
spending_money = int(raw_input("Spending money: "))

# calculate and print trip cost result
print trip_cost(city,days,spending_money)
