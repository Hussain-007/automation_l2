48. Create a Calculator with the following functions.

      a) Addition/subtraction/multiplication and division of two numbers 
         ( Note: Create separate function for each operation )
      b) Find square root of a given number.( Use keyword arguments in your function)
      c) Create a list of sub strings from a given string, such that sub strings are created with given character.
           That is, 
               string = "Pack: My: Box: With: Good: Food"
          Create sub strings with the delimiter character ":" such that the following sub strings are created.
                  substrlist=[Pack, My, Box, With, Good, Food]
           Note : Function should take at least 2 parameters ( Main string and delimiter character)
                          return value from function will be list of substring.
Ans:
import math
a, b = map(int, raw_input("Enter two numbers").split())
add = lambda a,b: a+b
sub = lambda a,b: a-b
mul = lambda a,b: a*b
div = lambda a,b: a/b
mod = lambda a,b: a%b
print "a+b",add(a,b)
print "a-b",sub(a,b)
print "a*b",mul(a,b)
print "a/b",div(a,b)
print "a%b",mod(a,b)

n = float(raw_input("Enter number whose sqroot is to be found:"))
sqroot = lambda n: math.sqrt(n)
print "sqrt(n)", sqroot(n)

string = "Pack: My: Box: With: Good: Food"
def substrlist(string, deli):
    return string.split(deli)
print substrlist(string, ": ")
