__doc__ = '''
Find the area of Circle given that radius of a circle. 
( Use pi value from Math module)
'''
import math
PI = math.pi

radius = int(input("Enter the Radius Of the Circle: "))
print("Area Of Circle: {:.02f}".format(PI*radius*radius))

if __name__ == '__main__':
    pass