'''35.Create Tuple as specified below 
a) Create a Tuple tup1 with days in a week & print the tuple elements 
b) Create a Tuple tup2 with months in a year and concatenate it with tup1 
c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater. 
d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 Notice the error type you get. 
e) Insert new element in to tuple by typecasting it to List'''
tup1=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
for each in tup1:
  print each
tup2=('January','February','March','April','May','June','July','August','September',
'October','November','December')
tupConcat=tup1+tup2
print "tupConcat=",tupConcat
tup1=(100,9,2,5,3)
tup2=(22,44,20,13,45,9)
tup3=(99,12,34,21,55)
if tup1>tup2 and tup1>tup3:
  print "Tup1 is the biggest"
elif tup2>tup1 and tup2>tup3:
  print "tup2 is the biggest"
else:
  print "tup3 is the biggest of all"
'''del tup1[2]
  Traceback (most recent call last):
  File "python", line 24, in <module>
TypeError: 'tuple' object doesn't support item deletion'''
del tup1
print tup1
'''Traceback (most recent call last):
  File "python", line 29, in <module>
NameError: name 'tup1' is not defined'''
tup2=list(tup2)
tup2.append(323)
print "Tup2 after appending a new item to this by typecasting it to List is",tup2
