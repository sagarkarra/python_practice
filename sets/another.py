'''
Input:
Write a program to remove duplicate element from other sequence.
Output:
print(type(t))
(10, 20, 30, 20, 10, 20, 30, 40)
<class 'tuple'>
(40, 10, 20, 30)
<class 'tuple'>

t=(10,20,30,20,10,20,30,40)
print(t)
print(type(t))
t=tuple(set(t))
print(t)
print(type(t))

Solution 2:
'''
def another_type():
    t=(10,20,30,20,10,20,30,40)
    print(t)
    print(type(t))
    t=tuple(set(t))
    print(t)
    print(type(t))
another_type()