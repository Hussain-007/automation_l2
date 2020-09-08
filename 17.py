__doc__ = '''Write program to find  the biggest  and Smallest of N numbers.
      PS: Use the functions to find biggest and  smallest numbers. 
'''
number_holder = []
limit = int(input("Enter the limit: "))
while limit > 0:
      number_holder.append(int(input("Enter the number: ")))
      limit -= 1

print(f"MAX: {max(number_holder)}")
print(f"MIN: {min(number_holder)}")

if __name__ == '__main__':
    pass