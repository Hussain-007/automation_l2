__doc__ = '''Using assignment operators, perform following operations
     Addition, Substation, Multiplication, Division, Modulus, Exponent and 
     Floor division operations'''
import math

def add(n1, n2):
    print(f"{n1} + {n2} : {n1+n2}")

def Subtract(n1, n2):
    print(f"{n1} - {n2} : {n1-n2}")

def Multiply(n1, n2):
    print(f"{n1} * {n2} : {n1*n2}")

def divide(n1, n2):
    print("{} / {} : {:.2f}".format(n1, n2, n1/n2))

def Modulus(n1, n2):
     print(f"{n1} % {n2} : {n1%n2}")

def Exponent(n1):
     print(f"Exponent of {n1} : {math.exp(n1)}")

def Floor_division(n1, n2):
     print(f"{n1} // {n2} : {n1//n2}")

     
if __name__ == '__main__':
     add(10,20)
     Subtract(20, 10)
     Multiply(10,3)
     divide(10,3)
     Modulus(10,3)
     Exponent(10)
     Floor_division(10,3)