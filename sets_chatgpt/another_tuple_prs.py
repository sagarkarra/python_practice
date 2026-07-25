'''
Input:
Remove duplicates from the tuple:
(1, 2, 2, 3, 4, 4, 5)
Output:
(1, 2, 2, 3, 4, 4, 5)
<class 'tuple'>
(1, 2, 3, 4, 5)
<class 'tuple'>

t=(1, 2, 2, 3, 4, 4, 5)
print(t)
print(type(t))
t=tuple(set(t))
print(t)
print(type(t))

Solution 2:
'''
def another_tuple_prs():
    t=(1, 2, 2, 3, 4, 4, 5)
    print(t)
    print(type(t))
    t=tuple(set(t))
    print(t)
    print(type(t))
another_tuple_prs()