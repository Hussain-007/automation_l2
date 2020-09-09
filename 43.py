'''43. Write a program to search given element from the list. Use your own function to search an element from list.
       Note: Function should receive variable length arguments and search each of these arguments present  in the  list.
'''

def findelement(list1,a):
    if a in list1:
        print("Element is Present")
    else:
        print("Element is absent")
        
list1 = input("Enter elements of list ")
a= input("Enter element to be searched")
findelement(list1,a)