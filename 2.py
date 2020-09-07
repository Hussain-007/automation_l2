__doc__ = 'Write a program to find the biggest of 3 numbers ( Use If Condition )'

def biggest_of_3numbers(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

if __name__ == '__main__':
    a, b, c = -20, -30, 5
    print(f"Biggest of {a}, {b}, {c} = {biggest_of_3numbers(a,b,c)}")