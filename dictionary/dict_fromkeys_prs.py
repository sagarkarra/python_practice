'''
Input:
Write a program to create a new dictionary with keys from sequence and values st to values by using
built-in function dict.fromkeys()
Output:
New dictionary:{'name': None, 'age': None, 'sex': None}
New dictionary:{'name': 10, 'age': 10, 'sex': 10}

s=('name','age','sex')
d=dict.fromkeys(s)
print("New dictionary:%s"% str(d))
d=dict.fromkeys(s,10)
print("New dictionary:%s"% str(d))

Solution 2:
'''
def dict_fromkeys_prs():
    d=dict.fromkeys(s)
    print("New dictionary:%s"% str(d))
    d=dict.fromkeys(s,10)
    print("New dictionary:%s"% str(d))
s=('name','age','sex')
dict_fromkeys_prs()
