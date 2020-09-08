__doc__ = '''Create a list of 5 names and check given name exist in the List.
        a) Use membership operator ( IN ) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction.
'''

name_list = ['Ronald','Timothy','Jason','Jeffrey','Ryan']

if 'Ronald' in name_list:
        print(f"Name is Present")
else:
        print("Name is Absent!")

for v in range(0, len(name_list)):
        if 'Ronal' == name_list[v]:
                print(f"Name is Present!")
                break
        else:
                print("Name is Absent!")
                break

print(f"List Before Reversal: {', '.join(name_list)}")
print(f"List in Reverse Order: {', '.join(name_list[::-1])}")