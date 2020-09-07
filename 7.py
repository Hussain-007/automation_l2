__doc__ = '''Create a list with at least 10 elements in it
       print all elements
       perform slicing
       perform repetition with * operator
       Perform concatenation wiht other list.
'''
aList = ['apt', '-get', 'install ', 'python', '*', 1, 2, 3, 4, 5]
bList = ['Kaptan', 'Aabid', 'Amrita','Aishwary', 'Gautam']

if __name__ == '__main__':
    #print length of list
    print(len(aList))
    #print all elements of list
    print(*aList)
    #print sliced element of list
    print(*aList[:4])
    #perform repetition with * operator
    print(aList[4]*10)
    #Perform concatenation with other list
    print(aList + bList)

