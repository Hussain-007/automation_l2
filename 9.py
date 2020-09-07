__doc__ = 'Write program to Add , subtract, multiply, divide 2 complex numbers.'


def add(n1, n2):
    print(f"{n1} + {n2} : {n1+n2}")

def Subtract(n1, n2):
    print(f"{n1} - {n2} : {n1-n2}")

def Multiply(n1, n2):
    print(f"{n1} * {n2} : {n1*n2}")

def divide(n1, n2):
    print("{} / {} : {:.2f}".format(n1, n2, n1/n2))

if __name__ == '__main__':
    #first complex number
    c1 = 3 + 6j
    #Second complex number
    c2 = 6 + 15j
    add(c1,c2)
    Subtract(c1, c2)
    Multiply(c1,c2)
 