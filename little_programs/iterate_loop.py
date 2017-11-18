# This program iterates through a loop

# declare a list
seasons = { "Fall", "Winter", "Spring", "Summer"}

# iterate list

print "First way to iterate: "
for season in seasons:
	print season

print "Second way to iterate: "
for i,season in enumerate(seasons):
	print "iteration {i} is {season}" .format(i = i, season = season) 
