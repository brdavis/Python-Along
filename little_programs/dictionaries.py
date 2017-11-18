# This program demonstrates dictionaries in python

# create a dictionary
groceries = {
	"apple": 1.00,
	"banana": 2.00,
	"cereal": 3.50
}

# different ways to print a dictionary

# print dictionary
print "\nPrints dictionary"
print groceries
  
# print list of dictionary entries
print "\nPrints list of dictionary"
print groceries.items()

# print dictionary keys
print "\nPrints dictionary keys"
print groceries.keys()

for item in groceries:
	print item

# print dictionary values
print "\nPrints dictionary values"
print groceries.values()

for item in groceries:
	print groceries[item]
