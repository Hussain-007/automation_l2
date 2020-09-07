__doc__ = 'Repeat program 7 with Tuple( Take example from Tutorial )'

aTuple = ('apt', '-get', 'install ', 'python', '*', 1, 2, 3, 4, 5)
bTuple = ('Kaptan', 'Aabid', 'Amrita','Aishwary', 'Gautam')

if __name__ == '__main__':
    #print length of Tuple
    print(len(aTuple))
    #print all elements of Tuple
    print(*aTuple)
    #print sliced element of Tuple
    print(*aTuple[:4])
    #perform repetition with * operator
    print(aTuple[4]*10)
    #Perform concatenation with other Tuple
    print(aTuple + bTuple)