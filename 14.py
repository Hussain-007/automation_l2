__doc__ = '''Write a program to create two list A and B such that List A 
           contains Employee Id, List B contains Employee name
     ( minimum 10 entries in each list ) and perform following operations
     a) Print all names on to screen
     b) Read the index from the  user and print the corresponding name from both list.
     c) Print the names from 4th position to 9th position
     d) Print all names from 3rd position till end of the list
     e) Repeat list elements by specified number of times ( N- times, where N is entered by user)
     f)  Concatenate two lists and print the output.
     g) Print element of list A and B side by side.( i.e.  List-A First element ,  List-B First element )
'''
aList = [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012]
bList = ['John','Aabid','Tommy','Mony','Venkit','Robert','Michael','William','David '	,
     'Richard','Joseph','Thomas','Charles']

# a) Print all names on to screen
print(', '.join(bList))
# b) Read the index from the  user and print the corresponding name from both list.
index_value = int(input("Enter the index value: "))
print(f"Emp_ID: {aList[index_value]}\nEmp_Name: {bList[index_value]}")
# c) Print the names from 4th position to 9th position
print(f"Names from 4th position to 9th position are {', '.join(bList[4:10])} ")
# d) Print all names from 3rd position till end of the list
print(f"Names from 3rd position till end of the list are {', '.join(bList[3:])} ")
# e) Repeat list elements by specified number of times ( N- times, where N is entered by user)
repeater_value = int(input("Enter the Repeater Value: "))
print(', '.join(bList * repeater_value))
# f)  Concatenate two lists and print the output.
cList = aList + bList
print(*cList)
# g) Print element of list A and B side by side.( i.e.  List-A First element ,  List-B First element )
for k,v in zip(aList, bList):
     print(k,v)
