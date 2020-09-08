__doc__ = '''
Write a program to check how many ovals present in the given string.
That is, count the number of " a e i o u" in the given string and
print the numbers against each oval.
Example :- "This is Python"
    Number of total ovals = 3
    i = 2
    o =1
'''
s = "This is Python".split()
s = ''.join(s)
s = list(s)
d = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}

for el in s:
    if el in d.keys():
        d[el] += 1

print(d)
if __name__ == '__main__':
    pass