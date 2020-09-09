__doc__ = '''31.Write a program to search an element in the list. i.e. 
Perform the binary search on the sorted list having integers as elements. 
If the search is successful print "Success" else print "un successful search".'''

str1=input("Enter the numbers")
list1=list(str1)
list1.sort()
print("The sorted order list1 of elements is",list1)
searchElement = int(input("Enter the element tosearch from the above list"))
found=0
for each in list1:
  if each == searchElement:
    print("Successful")
    found=1
    break
if found == 0:
  print("Unsuccessful search")