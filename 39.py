'''39.Using Time and Calendar module ,Print current date and time. Print current month calendar.'''
import time
localtime = time.asctime(time.localtime(time.time()))
print "Local current time :", localtime

import calendar
cal = calendar.month(2017,10)
print "\nHere is the calendar:"
print cal
