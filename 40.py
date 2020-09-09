'''40.Using time module perform following operations. 
a) print(current time for every 5 seconds up to 1 minute time interval. 
b) Write a program to find out how much CPU time is taken for the execution of above(40.a) program.'''
import time
i=12
while i>0:
  localtime = time.asctime(time.localtime(time.time()))
  print("Local current time :", localtime)
  time.sleep(5)
  i=i-1