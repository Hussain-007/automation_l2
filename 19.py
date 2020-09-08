__doc__ = '''Using loop structures print even numbers between 1 to 100.  
     a) By using For loop , use continue/ break/ pass statement to skip  odd numbers.
           i)  break the loop if the value is 50
           ii) Use continue for the values 10,20,30,40,50

     b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
            i)  break the loop if the value is 90
           ii) Use continue for the values 60,70,80,90
'''
print("===Even Number List WHILE LOOP===")
m = 1
while m < 101:

      if m == 90:
            break
      m += 1
      if m%2:
            continue  
      if m == 60 or m == 70 or m == 80 or m == 90:
            continue      
      print(m)

print("===Even Number List FOR LOOP===")
for n in range(1,101):

      if n%2:
            continue
      if m == 60 or m == 70 or m == 80 or m == 90:
            continue
      print(n)
      if n == 50:
            break

