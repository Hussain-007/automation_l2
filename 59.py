59. Create file called  "stringop.py" which has following functions
             i) functions to sort numbers( Use loops for  sorting, do not use built in function)
             ii)  function to search given element through binary search method.
                 ( Refer to net for the Binary search algorithm)
            iii) function to reverse the given string 
        
         Write new program in file strpackage.py such that you import functions of file  "stringop.py" to your new program
Ans:
#stringop.py
def list_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print "Sorted:", arr
    
def binarySearch(list1, item):
    list1.sort()
    first = 0
    last = len(list1)-1
    found = False
    
    while first<=last and not found:
        midpoint = (first+last)/2
        if list1[midpoint] == item:
            found = True
            return found
        else:
            if item < list1[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def list_rev(l):
    print l.reverse()
    print "reversed:", l

# strpackage.py
from stringop import*
list_sort([23,81,42,51,31])
print "binarySearch([23,81,42,51,31]):", binarySearch([23,81,42,51,31])
list_rev([23,81,42,51,31])
output:
Sorted: [23, 31, 42, 51, 81]
binarySearch([23,81,42,51,31],51): True
None
reversed: [81, 51, 42, 31, 23]
