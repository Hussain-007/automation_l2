__doc__ = '''
Write a program to receive 5 command line arguments and print each argument separately.
Example :
             >> python test.py arg1 arg2 arg3 arg4 arg5
  a) From the above statement your program should receive arguments and print them each of them. 
  b) Find the biggest of three numbers, where three numbers are passed as command line arguments.
'''
import argparse
import sys

arg = []
def print_cli(return_cap=False):
    global arg
    if len(sys.argv):
        arg = sys.argv[1:]
        if return_cap:
            return arg
        for sl, item in enumerate(arg,1):
            print(f"arg{sl} -> {item}")
    else:
        print("*********************************************\n")
        print("There is no arguments provided in the program!")
        print("\n*********************************************\n")

def biggest_of_3numbers():    
    num_list = print_cli(return_cap=True)
    if len(num_list) == 3:
        n1, n2, n3 = [int(x) for x in num_list]
        if n1 > n2 and n1 > n3:
            return n1, n2, n3, n1
        elif n2 > n1 and n2 > n3:
            return n1, n2, n3, n2
        else:
            return n1, n2, n3, n3
    else:
        print(num_list)


if __name__ == '__main__':
    a,b,c,d = biggest_of_3numbers()
    print(f"The Biggest among {a}, {b}, {c} : {d}")
    