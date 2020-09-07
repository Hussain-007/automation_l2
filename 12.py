__doc__ = '''Read 10 numbers from user and find the average of all.
a) Use comparison operator to check how many numbers are less than average and print them
b) Check how many numbers are more than average.
c) How many are equal to average.
'''
less_than_avg = []
greater_than_avg = []
equal_to_avg = []
n = list(range(2, 13))
avg = sum(n)/len(n)
print(f"Average: {avg}")
for item in n:
    if item > avg:
        less_than_avg.append(item)
    elif item < avg:
        greater_than_avg.append(item)
    else:
        if item == avg:
            equal_to_avg.append(item)

print("Numbers less than Average Value: {}".format(', '.join([str(x) for x in less_than_avg])))
print("Numbers greater than Average Value: {}".format(', '.join([str(x) for x in greater_than_avg])))
print("Numbers Equal to Average Value: {}".format(', '.join([str(x) for x in equal_to_avg])))

