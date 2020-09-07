__doc__ = 'Write a program to find the number is Prime or not.'

def find_prime(num):
    if num == 1 or num == 0 or not num%2:
        return "Not Prime"

    if num == 2:
        return "Prime"
    if num%2:
        for sub_num in range(3, num, 2):
            if not num%sub_num:
                return "Not Prime"
        else:
            return "Prime"

if __name__ == '__main__':
    print(find_prime(99))