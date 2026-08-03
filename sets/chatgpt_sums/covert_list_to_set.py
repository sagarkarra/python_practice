'''
Input:
Create a set containing:
100, "Python", True, 3.14
Output:
{True, 'Python', 3.14, 100}

s=set([100, "Python", True, 3.14])
print(s)

Solution 2: 
'''
def set_different(list1):
    s=set(list1)
    return s
list1=[100, "Python", True, 3.14]
output1=set_different(list1)
print(output1)