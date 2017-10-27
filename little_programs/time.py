from datetime import datetime
now = datetime.now()

# print year, month,day
print "%s-%s-%s" % (now.year, now.month, now.day)

#print year, month, day, hour, minute, second
print '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second) 
