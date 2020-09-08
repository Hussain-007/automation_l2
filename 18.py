__doc__ = '''Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1.( reverse printing)
     a) By using For loop 
     b) By using while loop
    c) Let    mystring ="Hello world"
             print each character of  mystring in to separate line using appropriate  loop structure.
'''
for n in range(1, 101):
    print(f"Number: {n}")

print("\n<---FOR LOOP Reverse Number--->")
for n in range(100, 0,-1):
    print(f"Number: {n}")

n = 1
print("\n<---WHILE LOOP--->")
while n < 101:
    print(f"Number: {n}")
    n += 1

print("\n<---WHILE LOOP Reverse Number--->")
n = 100
while n > 0:
    print(f"Number: {n}")
    n -= 1


mystring ="Hello world"
print(*mystring, sep='\n')

if __name__ == '__main__':
    pass