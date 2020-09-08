__doc__ = '''
Apply all built in functions on str1ings in your program.
Note there are 40  str1ing functions. Use Tutorial for the help. 
Note: Each program should have 5 str1ing built in functions 
( so write 8 programs to cover all str1ing functions)
'''
str1= "this is a str1ing"
print("str1.capitalize():",str1.capitalize())
print("str1.center(60,'x'):",str1.center(60,'x'))
sub = "i";
print("str1.count(sub,1,30):",str1.count(sub,1,30))
sub = "wow";
print("str1.count(sub):",str1.count(sub))

str1= str1.encode()
print("Encoded str1ing:",str1)
print("Decoded str1ing:",str1.decode(),'\n')

#2.Second 5 str1ing built in functions
str1= "this is a str1ing"
suffix = "ing"
print("str1.endswith(suffix):",str1.endswith(suffix))
print("str1.endswith(suffix,10):",str1.endswith(suffix,10))
suffix = "i"
print("str1.endswith(suffix, 1, 4):",str1.endswith(suffix, 1, 4))
print("str1.endswith(suffix, 2, 6):",str1.endswith(suffix, 2, 6))

print("\nOriginal str1ing:",str1)
print("Default exapanded tab:",str1.expandtabs() )
print("Double exapanded tab:",str1.expandtabs(16))

str12 = "ng"
print("\nstr1.find(str12):",str1.find(str12))
print("str1.find(str12, 10):",str1.find(str12, 10))
print("str1.find(str12, 40):",str1.find(str12, 40))

print("\nstr1.index(str12):",str1.index(str12))
print("str1.index(str12, 10):",str1.index(str12, 10))
#print("str1.index(str12, 40):",str1.index(str12, 40))

str1= "this2009"
print("\nstr1.isalnum():",str1.isalnum())
str1= "this is a str1ing";
print("str1.isalnum():",str1.isalnum())



#3.Third set of 5 str1ing built in functions
str1= "this";  # No space & digit in this str1ing
print("\nstr1.isalpha():",str1.isalpha())
str1= "this is str1ing example";
print("str1.isalpha():",str1.isalpha())

str1= "123456";  # Only digit in this str1ing
print("\nstr1.isdigit():",str1.isdigit())

str1= "this is str1ing example..";
print("\nstr1.isdigit():",str1.isdigit())

str1= "THIS is str1ing example"; 
print("\nstr1.islower():",str1.islower())
str1= "this is str1ing example";
print("str1.islower()",str1.islower())

str1= u"this2009";  # u stands for Unicode.One must prefix u to check for isnumeric
print("\nstr1.isnumeric():",str1.isnumeric())
str1= u"23443434";
print("str1.isnumeric():",str1.isnumeric())

str1= "       "; 
print("\nstr1.isspace():",str1.isspace())
str1= "This is str1ing example";
print("str1.isspace():",str1.isspace())



#4.Fourth set of 5 str1ing built in functions
str1= "This Is str1ing Example";
print("\nstr1.istitle():",str1.istitle())
str1= "This is str1ing example";
print("str1.istitle():",str1.istitle())

str1= "THIS IS str1ING EXAMPLE"; 
print("\nstr1.isupper():",str1.isupper())
str1= "THIS is str1ing example";
print("str1.isupper():",str1.isupper())

s = "-";
seq = ('a','b','c'); # This is sequence of str1ings.
print("\ns.join(seq):",s.join(seq))

str1= "this is str1ing example";
print("\nLength of the str1ing:",len(str1))

print("\nstr1.ljust(50, '1')",str1.ljust(50, '1'))



#5.Fifth set of 5 str1ing built in functions
str1= "THIS IS str1ING EXAMPLE";
print("\nstr1.lower():",str1.lower())

str1= "     this is str1ing example    ";
print("\nstr1.lstr1ip():",str1.lstrip())
str1= "88888888this is str1ing example8888888";
print("\nstr1.lstr1ip('8'):",str1.lstrip('8'))


# Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
trantab = str1.maketrans(intab, outtab)
str1 = "this is str1ing example....wow!!!"
print("\nstr1.translate(trantab):",str1.translate(trantab))

str1= "this is really a  frozen str1ing example";
print("\nMax character: ",max(str1))
str1= "this is a str1ing example";
print("Max character: ",max(str1))

str1= "this-is-real-str1ing!example";
print("\nMin character: " + min(str1))
str1= "this-is-a-str1ing-example";
print("Min character: " + min(str1))



#6.Sixth set of 5 str1ing built in functions
str1= "this is str1ing example....wow!!! this is really str1ing"
print(str1.replace("is", "was"))
print(str1.replace("is", "was", 3))

str1 = "this is really a str1ing example....wow!!!";
str12 = "is";
print(str1.rfind(str12))
print(str1.rfind(str12, 0, 10))
print(str1.rfind(str12, 10, 0))
print(str1.find(str12))
print(str1.find(str12, 0, 10))
print(str1.find(str12, 10, 0))

str1 = "this is str1ing example....wow!!!";
str12 = "is";
print(str1.rindex(str12))
print(str1.index(str12))

str1= "this is str1ing example....wow!!!";
print(str1.rjust(50, '0'))

str1= "     this is str1ing example....wow!!!     ";
print(str1.rstrip())
str1= "88888888this is str1ing example....wow!!!8888888";
print(str1.rstrip('8'))



#7.Seventh set of 5 str1ing built in functions
str1= "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str1.split( ))
print(str1.split(' ', 1 ))

str1= "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print(str1.splitlines( ))
print(str1.splitlines( 0 ))
print(str1.splitlines( 3 ))
print(str1.splitlines( 4 ))
print(str1.splitlines( 5 ))

str1= "this is str1ing example....wow!!!";
print(str1.startswith( 'this' ))
print(str1.startswith( 'is', 2, 4 ))
print(str1.startswith( 'this', 2, 4 ))

str1= "0000000this is str1ing example....wow!!!0000000";
print(str1.strip( '0' ))

str1= "this is str1ing example....wow!!!";
print(str1.swapcase())
str1= "THIS IS str1ING EXAMPLE....WOW!!!";
print(str1.swapcase())



#8.Eighth set of 5 str1ing built in functions
str1= "this is str1ing example!!!";
print("\nstr1.title():",str1.title())

# from str1ing import maketrans   # Required to call maketrans function.
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str1= "this is str1ing example";
print(str1.translate(trantab))

str1= "this is str1ing example";
print("\nstr1.capitalize():",str1.upper())

str1= "this is str1ing example";
print("\nstr1.zfill(40):",str1.zfill(40))
print("str1.zfill(50):",str1.zfill(50))

str1= u"this2009";  
print("\nstr1.isdecimal():",str1.isdecimal())
str1= u"23443434";
print("str1.isdecimal():",str1.isdecimal())



if __name__ == '__main__':
    pass