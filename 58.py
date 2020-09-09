58. Create file called  "calc.py" which has following functions
             i) functions to add 2 numbers
             ii)  function to find diff of 2 numbers
            iii) function to multiply 2 numbers
           iv) all maths operations ( Sqrt, div, floor div, modulus, primnumber)
           v) Fibonacci series
        
        a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
        b) Use From <module> import <function> statement to import only few function  from calc module.
Ans:
#calc.py
from __future__ import division
import math

def add(a,b):
    print "a+b:", a+b
    
def diff(a,b):
    print "a-b:", a-b
    
def multiply(a,b):
    print "a*b:", a*b
    
def sqroot(a):
    print "sqrt(a)", math.sqrt(a)
    
def floor_div(a,b):
    print "a//b:", a//b
    
def division(a,b):
    print "a/b:", a/b
    
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

def isprime(n):
    for i in range(2,):
        if n%i==0:
            print n,"not prime"
            break
        else:
            print n,"is prime"
            break
n=int(raw_input())        
isprime(n)        

#math.py
from calc import*
add(23,15)
diff(45,12)
multiply(3,4)
sqroot(25)
floor_div(9,2)
division(5,4)
fib_series(10)
print "prime_check:", isprime(10)
