'''44. Write a program with lambda function to perform following.
         a) Perform all the operations of basic calculator ( add, sub, multiply, divide, modulus, floor division )
'''
a, b = map(int, raw_input("Enter two numbers").split())
add = lambda a,b: a+b
sub = lambda a,b: a-b
mul = lambda a,b: a*b
div = lambda a,b: a/b
mod = lambda a,b: a%b
print("a+b",add(a,b))
print("a-b",sub(a,b))
print("a*b",mul(a,b))
print("a/b",div(a,b))
print("a%b",mod(a,b))