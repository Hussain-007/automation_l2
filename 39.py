'''39.Using Time and Calendar module ,print(current date and time. print(current month calendar.'''
import time
import calendar

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)
cal = calendar.month(2017,10)
print("\nHere is the calendar:")
print(cal)
