__doc__ = '''
Using the built in functions on Numbers perform following operations
     a) Round of the given floating point number 
             example :  n=0.543  then round it next decimal number , i.e n=1.0
              Use round() function
      b) Find out the square root of a given number. ( use sqrt(x) function)
      c) Generate random number between 0, and 1 ( use  random() function)  
      d)  Generate random number between 10 and  500. ( use uniform() function)
     e) Explore all Math and Random module functions  on a given number/ List. 
     ( Refer to tutorial  for Math & Random functions list)
'''
import math
import random
n=0.543
print(round(n))
print(math.sqrt(4))
result = random.random()
print(result)

result = random.uniform(10,500)
print(result)
if __name__ == '__main__':
    pass