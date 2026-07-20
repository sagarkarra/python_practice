'''
Input:
Write a program to return a shallow copy of dictionary dict using the dictionary built-in function call
d.copy()
Output:
New dictionary: {'Name': 'Manni', 'Age': 7, 'Class': 'First'}

d={'Name':"Manni",'Age':7,'Class':"First"}
d1=d.copy()
print("New dictionary:",d1)

Solution 2:
'''
def dict_copy():
    d1=d.copy() 
    print("New dictionary:",d1) 
d={'Name':"Manni",'Age':7,'Class':"First"}
dict_copy()