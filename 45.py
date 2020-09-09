45. Write a program to check given string is Palindrome or not. ( Use function Concepts and Required keyword, Default parameter concepts)
       That is reverse the given string and check whether it is same as original string, if so then it is palindrome.
       Example : String = "Malayalam"  reverse string = "Malayalam" hence given string is palindrome.
Ans:
def isPal(s):
    if s == s[::-1]:
        print s,"is a palindrome"
    else:
        print s,"is NOT a palindrome"
s=raw_input("enter atring")
isPal(s)