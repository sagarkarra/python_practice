'''
Input:
d1={10:'Python',20:'Django',30:'C++',40:'C'}
Output:
dict_keys([10, 20, 30, 40])
<class 'dict_keys'>
10
20
30
40
d1={10:'Python',20:'Django',30:'C++',40:'C'}
k=d1.keys()
print(k)
print(type(k))
for k in d1.keys():
    print(k)

Solution 2:
'''
def dict_keys():
    k=d1.keys()
    print(k)
    print(type(k))
    for k in d1.keys():
        print(k)
d1={10:'Python',20:'Django',30:'C++',40:'C'}
dict_keys()