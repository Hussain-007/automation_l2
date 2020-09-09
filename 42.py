42. Write a program to generate a Fibonacci series using a function called fib(n), 
       a) where  N is user specified argument specifies number of elements in the series.
Ans
def fib_series(n):
    first = 0
    second= 1
    
    third = 0
    while(n>third):
        print first,
        total = first + second
        first = second
        second = total
        third += 1

n = int(raw_input().split())
fib_series(n)

43. Write a program to search given element from the list. Use your own function to search an element from list.
       Note: Function should receive variable length arguments and search each of these arguments present  in the  list.
Ans:
def findelement(list1,a):
    if a in list1:
        print "Element is Present"
    else:
        print "Element is absent"
        
list1 = input("Enter elements of list ")
a= input("Enter element to be searched")
findelement(list1,a)