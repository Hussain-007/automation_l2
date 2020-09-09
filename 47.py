'''47. Write function to extend the tuple with elements of list. 
Pass list and Tuple as parameter to the function.
'''
def tup_extend(tup1,list1):
    tup3 = tup1+tuple(list1)
    print(tup3)
    
tup1=(1,'hello',2,'paris')
list1=[3,'world',4,'tour']
tup_extend(tup1,list1)