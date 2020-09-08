__doc__ = '''
Write a program to check given string is Palindrome or not.
That is reverse the given string and check whether it is same as original string, 
if so then it is palindrome.
Example : String = "malayalam"  reverse string = "malayalam" hence given 
string is palindrome.
Use built functions to check given string  is palindrome or  not.
'''
myStr = input("Enter the string: ")
#myStr="Hello buddy"
myStr1 = myStr[::-1]
if myStr == myStr1:
  print("The given string ",myStr," is palindrome")
else:
  print("The given string ",myStr," is not palindrome")

if __name__ == '__main__':
    pass