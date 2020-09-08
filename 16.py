__doc__ = '''Write program to perform following:
     i) Check whether given number is prime or not.
    ii) Generate all the prime numbers between 1 to N where N is given number.
'''

def find_prime(num):
    if num == 2:
        return True
    if num == 1 or num == 0 or not num%2:
        return False    
    if num%2:
        for sub_num in range(3, num, 2):
            if not num%sub_num:
                return False
        else:
            return True

if __name__ == '__main__':
    prime_holder = []
    val = int(input("Enter a number to check Prime: "))
    if find_prime(val):
        print(f"{val} is Prime")
    else:
        print(f"{val} is NOT Prime")
    limit = int(input("Enter the limit to print all the prime: "))
    for n in range(1, limit):
        if find_prime(n):
            prime_holder.append(n)
    print(f"Prime: {prime_holder}")