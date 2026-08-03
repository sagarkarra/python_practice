'''
Input:
Write a program to remove the last key and value pair from Non-Empty Dictionary by using the function
popitem()
Output:
{10: 1.2, 20: 3.4, 30: 1.2, 40: 4.5}
<class 'dict'>
2418851528640
{10: 1.2, 20: 3.4, 30: 1.2}
<class 'dict'>
2418851528640
{10: 1.2, 20: 3.4}
<class 'dict'>
2418851528640
{10: 1.2}
<class 'dict'>
2418851528640
{}
<class 'dict'>
2418851528640
KeyError: 'popitem(): dictionary is empty'

d = {10:1.2,20:3.4,30:1.2,40:4.5}
print(d)
print(type(d))
print(id(d))
d.popitem()
print(d)
print(type(d))
print(id(d))
d.popitem()
print(d)
print(type(d))
print(id(d))
d.popitem()
print(d)
print(type(d))
print(id(d))
d.popitem()
print(d)
print(type(d))
print(id(d))
d.popitem()
print(d)
print(type(d))
print(id(d))
d.popitem()

Another method:
d.popitem()
{}.popitem()
dict().popitem()

Solution 2:
'''
def popitem_prs():
    print(d)
    print(type(d))
    print(id(d))
    d.popitem()
    print(d)
    print(type(d))
    print(id(d))
    d.popitem()
    print(d)
    print(type(d))
    print(id(d))
    d.popitem()
    print(d)
    print(type(d))
    print(id(d))
    d.popitem()
    print(d)
    print(type(d))
    print(id(d))
    d.popitem()
    print(d)
    print(type(d))
    print(id(d))
    d.popitem()
d = {10:1.2,20:3.4,30:1.2,40:4.5}
popitem_prs()