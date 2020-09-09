'''32.Write a program to perform following operations on List. 
Create 3 lists List1,List2 and List3 
a. Find the length of each list and print(it 
b. Find the maximum and minimum element of each list 
c. Compare each list and determine which list is biggest & which list is smallest. 
d. Delete first and last element of each list and print(list contents.'''
list1=[1,2,3,4,5,6,7]
list2=['a','b','c','d','e']
list3=['abc','def','edd']
print(list1)
print(list2)
print(list3)
print("Length of list1=",len(list1))
print("Length of list2=",len(list2))
print("Length of list3=",len(list3))
print("Max of list1=",max(list1))
print("Min of list1=",min(list1))
print("Max of list2=",max(list2))
print("Min of list2=",min(list2))
print("Max of list3=",max(list3))
print("Min of list3=",min(list3))
if list1>list2 and list1>list3:
  print("\nlist1 is the biggest",list1)
elif list2>list1 and list2>list3:
  print("\nlist2 is the biggest",list2)
else:
  print("\nlist3 is the biggest",list3)
  
if list1<list2 and list1<list3:
  print("\nlist1 is the smallest",list1)
elif list2<list1 and list2<list3:
  print("\nlist2 is the smallest",list2)
else:
  print("\nlist3 is the smallest",list3)

print("\nList1 before removing 1st and last element using Pop method")
print(list1)
print("\nList1 after removing 1st and last element using pop method")
list1.pop(0);list1.pop(-1)
print(list1)
print("List2 before removing 1st and last element using Pop method")
print(list2)
print("List2 after removing 1st and last element using pop method")
list2.pop(0);list2.pop(-1)
print(list2)
print("List3 before removing 1st and last element using Pop method")
print(list3)
print("List3 after removing 1st and last element using pop method")
list3.pop(0);list3.pop(-1)
print(list3)
