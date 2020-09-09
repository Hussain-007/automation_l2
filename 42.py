'''42. Write a program to generate a Fibonacci series using a function called fib(n), 
       a) where  N is user specified argument specifies number of elements in the series.
       '''


def fib_series(n):
    first = 0
    second= 1
    
    third = 0
    while(n>third):
        print(first,)
        total = first + second
        first = second
        second = total
        third += 1

n = int(raw_input().split())
fib_series(n)
