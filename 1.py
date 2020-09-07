__doc__ = 'Write a program to add , Subtract, Multiply, and divide 2 numbers'

def add(n1, n2):
    print(f"{n1} + {n2} : {n1+n2}")

def Subtract(n1, n2):
    print(f"{n1} - {n2} : {n1-n2}")

def Multiply(n1, n2):
    print(f"{n1} * {n2} : {n1*n2}")

def divide(n1, n2):
    print("{} / {} : {:.2f}".format(n1, n2, n1/n2))

if __name__ == '__main__':
    add(10,20)
    Subtract(20, 10)
    Multiply(10,3)
    divide(10,3)