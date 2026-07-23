'''
Input:
d={'Name':"Vani",'Age':7}
Output:
Value: dict_items([('Name', 'Vani'), ('Age', 7)])
{'sno': 101, 'sname': 'rama', 'm1': 36, 'm2': 65, 'm3': 56}
<class 'dict'>
dict_items([('sno', 101), ('sname', 'rama'), ('m1', 36), ('m2', 65), ('m3', 56)])

dict={'Name':"Vani",'Age':7}
print("Value: %s" %dict.items())
d={'sno':101,'sname':'rama','m1':36,'m2':65,'m3':56}
print(d)
print(type(d))
print(d.items())

Solution 2:
'''
def dict_items():
    print("Value: %s" %dict.items())
    print(d)
    print(type(d))
    print(d.items())
dict={'Name':"Vani",'Age':7}
d={'sno':101,'sname':'rama','m1':36,'m2':65,'m3':56}
dict_items()