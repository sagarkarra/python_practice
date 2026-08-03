'''
Input:
1)dict={'sex':"Female",'Age':7,'Name':'Vani'}
2)d1={10:'Python',20:'Django',30:'C++',40:'C'}
Output:
Values: ['Female', 7, 'Vani']
{10: 'Python', 20: 'Django', 30: 'C++', 40: 'C'}
<class 'dict'>
dict_values(['Python', 'Django', 'C++', 'C'])
<class 'dict_values'>
Python
Django
C++
C
Python
Django
C++
C

dict={'sex':"Female",'Age':7,'Name':'Vani'}
print("Values:",list(dict.values()))
d1={10:'Python',20:'Django',30:'C++',40:'C'}
print(d1)
print(type(d1))
vs=d1.values()
print(vs)
print(type(vs))
for v in vs:
    print(v)
for v in d1.values():
    print(v)

Solution 2:
'''
def dict_values():
    print("Values:",list(dict.values()))
    print(d1)
    print(type(d1))
    vs=d1.values()
    print(vs)
    print(type(vs))
    for v in vs:
        print(v)
    for v in d1.values():
        print(v)
dict={'sex':"Female",'Age':7,'Name':'Vani'}
d1={10:'Python',20:'Django',30:'C++',40:'C'}
