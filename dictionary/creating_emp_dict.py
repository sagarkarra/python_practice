'''
Input:
Write a program to create a empty dictionary and later
add the key value pairs.
Output:
{}
<class 'dict'>

{'sno': 101, 'snname': 'rama', 'm1': 65, 'm2': 76, 'm3': 85}
<class 'dict'>

s={}
print(s)
print(type(s))
print()
s['sno']=101
s['snname']="rama"
s['m1']=65
s['m2']=76
s['m3']=85
print(s)
print(type(s))

Solution 2:
'''
def create_emp_dict():
    s={}
    print(s)
    print(type(s))
    print()
    s['sno']=101
    s['snname']="rama"
    s['m1']=65
    s['m2']=76
    s['m3']=85
    print(s)
    print(type(s))  
create_emp_dict()