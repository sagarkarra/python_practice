'''
Input:
Write a program to remove Key,Value pair from Non-Empty Dictionary Object.If value of key does not exis
t the we get KeyError.
Output:
{10: 1.2, 20: 3.4, 30: 1.2, 40: 4.5, 50: 3.4}
<class 'dict'>
1982599479232
{10: 1.2, 20: 3.4, 40: 4.5, 50: 3.4}
<class 'dict'>
1982599479232
{10: 1.2, 40: 4.5, 50: 3.4}
<class 'dict'>
1982599479232
{10: 1.2, 40: 4.5}
<class 'dict'>
1982599479232
d1.pop(120)  KeyError: 120

d1=d1={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4}
print(d1)
print(type(d1))
print(id(d1))
d1.pop(30)
print(d1)
print(type(d1))
print(id(d1))
d1.pop(20)
print(d1)
print(type(d1))
print(id(d1))
d1.pop(50)
print(d1)
print(type(d1))
print(id(d1))
d1.pop(120)
{}.pop(10)
dict().pop(20)

Solution 2:
'''
def pop_function():
    print(d1)
    print(type(d1))
    print(id(d1))
    d1.pop(30)
    print(d1)
    print(type(d1))
    print(id(d1))
    d1.pop(20)
    print(d1)
    print(type(d1))
    print(id(d1))
    d1.pop(50)
    print(d1)
    print(type(d1))
    print(id(d1))
    d1.pop(120)
    {}.pop(10)
    dict().pop(20)
d1={10: 1.2, 20: 3.4, 30: 1.2, 40: 4.5, 50: 3.4}
pop_function()