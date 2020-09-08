__doc__ = '''
Write a program to Sort given N numbers 
( Use only loop structures and Conditions to sort the elements. 
Use Bubble sort / Selection sort technique to sort the elements of List)
Note : don't use built in functions to sort.
'''
str1=input("Enter the numbers: ")
list1=list(str1)
for each in range(len(list1)):
  swap=False
  i = 0
  while i<len(list1)-1:
    if list1[i]>list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i]
      swap = True
    i = i+1
  if swap == False:
    break
print (list1)

if __name__ == '__main__':
    pass