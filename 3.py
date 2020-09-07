__doc__ = 'Write a program to find  given number is odd or Even'

def even_odd(num):
    if num % 2:
        return 'Odd'

    else:
        return 'Even'

if __name__ == '__main__':
    num = 10
    print(f"Even/Odd for {num} = {even_odd(num)}")