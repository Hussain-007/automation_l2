41. Using calendar module perform following operations.
           a)print the 2016 calendar with space between months as 10 character.
           b) How many leap days between the years 1980 to 2025.
           c) Check given year is leap year or not. 
           d) print calendar of any specified month of the year 2016.
Ans:
import calendar
for months in range(1,13):
    print calendar.month(2016,months)
print
print "Leap days between 1980 to 2025:", calendar.leapdays(1980, 2026)
print "2017 is leap year:", calendar.isleap(2017)
print "month of 2016:",calendar.month(2016,3)