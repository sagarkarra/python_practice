''''
Input:
Write a program to create a empty dictionary add the same dict name but diff dict values.
Output:
{}
<class 'dict'>
Before a,b value: {'a': 10, 'b': 20}
After a,b,c value: {'a': 100, 'b': 50, 'c': 30}
Final values of dict is: {'a': 100, 'b': 50, 'c': 30}
<class 'dict'>

d={}
print(d)
print(type(d))
d['a']=10
d['b']=20
print("Before a,b value:",d)
d['c']=30
d['a']=100
d['b']=50
print("After a,b,c value:",d)
print("Final values of dict is:",d)
print(type(d))

Solution 2:
'''
def add_values_twice():
    d={}
    print(d)
    print(type(d))
    d['a']=10
    d['b']=20
    print("Before a,b value:",d)
    d['c']=30
    d['a']=100
    d['b']=50
    print("After a,b,c value:",d)
    print("Final values of dict is:",d)
    print(type(d))
add_values_twice()