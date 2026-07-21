'''
Input:
Write a program to obtain the value by passing the value of key,then we get None as result.This should
be done by using dict.get() 
Output:
{10: 1.2, 20: 3.4, 30: 1.2, 40: 4.5, 50: 3.4}
<class 'dict'>
1.2
3.4

d1={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4}
print(d1)
print(type(d1))
val=d1.get(10)
print(val)
val=d1.get(20)
print(val)

Solution 2:
'''
def another_dict_get_prs():
    print(d1)
    print(type(d1))
    val=d1.get(10)
    print(val)
    val=d1.get(20)
    print(val)
d1={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4}
another_dict_get_prs()