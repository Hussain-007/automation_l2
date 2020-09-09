46. Write a function to find the  biggest of 4 numbers.
       a) All numbers are passed as arguments separately ( Required argument)
       b) use default values for arguments  ( Default arguments)
Ans:
def biggestnum(a,b,c,d):
    if a>=b and a>=c and a>=d:
        print a, "is largest"
    elif b>=a and b>=c and b>=d:
        print b ,"is largest"
    elif c>=a and c>=b and c>=d:
        print c, "is largest"
    else:
        print d, "is largest"

biggestnum(43,56,2,76)