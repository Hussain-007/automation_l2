'''38.Create 2 dictionaries as follows 
dict1 ={'Name':'Ramakrishna','Age':25} 
dict2={'EmpId':1234,'Salary':5000} 
Perform following operations 
a) Create single dictionary by merging dict1 and dict2 
b) Update the salary to 10% 
c) Update the age to 26 
d) Insert the new element with key "grade" and assign value as "B1" 
e) Extract and print(all values and keys separately. 
f) delete the element with key 'Age' and print(dictionary elements.'''
dict1 ={'Name':'Ramakrishna','Age':25} 
dict2={'EmpId':1234,'Salary':5000}
dict1.update(dict2)
print("After merging dict1and dict2, the single dict is",dict1)
dict1['Salary']='5500'
print("\nthe dict after updating salary to 10% is now",dict1)
dict1['Age']=26
print("\nthe dict after updating age to 26 is now",dict1)
dict1['Grade']='B1'
print("\nNow the dict is",dict1)
print("The keys of dict separately is",dict1.keys())
print("The values of dict separately is",dict1.values())
del dict1['Age']
print("\nDict after deleting element with key Age is",dict1)
