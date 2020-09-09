'''33.Create a list with 7 elements and perform following operations. 
Let List=[10,20,30,40,50,60,70] 
a) Append an object 80 to the List 
b) insert object 100 at 4th position 
c) Sort the list and print(all elements 
d) Sort the elements of the list in descending order. 
e) delete last three elements using pop operation'''
List=[10,20,30,40,50,60,70]
print(List)
List.append(80)
print("The Appended list is",List)
List.insert(3,100)
print("The list after inserting 100 at 4th position is",List)
List.sort()
print("List after sorting is",List)
List.reverse()
print("The list in descending order",List)
List.pop()
List.pop()
List.pop()
print("List after removing last 3 elements",List)
