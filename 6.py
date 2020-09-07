__doc__ = '''Write a program to read string and print each character separately.
    a) Slice the string using slice operator [:] slice the portion the strings 
        to create a sub strings.
    b) Repeat the string 100 times using repeat operator *
    c) Read strig 2 and  concatenate with other string using + operator.
'''
def str_slice(str_input):    
    for ch in list(str_input):
        print(ch, sep=' ')

def str_slice_op(str_input, substr_len):
    print(f"String: {str_input} and SubStrings: {str_input[:substr_len]} - {str_input[substr_len:]}")

def str_repeate(repeater=None):
    if repeater != None:        
        print("*"*int(repeater))
    else:
        str_repeate(int(input("Enter the repater Count: ")))

def str_concate():
    str1 = input("Enter the First String: ")
    str2 = input("Enter the Second String: ")
    print(f"{str1} + {str2} : {str1 + str2}")


if __name__ == '__main__':
    str_input = input("Enter the string: ")
    str_slice(str_input)
    str_slice_op(str_input, 2)
    str_repeate()
    str_concate()