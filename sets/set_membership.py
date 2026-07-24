'''
Input:
Write a program to check whether the given element is there or not using the in or not operator.
Output:
True
False
False
False
False
True
False

se1={10,20,30,True,100,'Parayana','Python'}
print('Parayana' in se1)
print('Django' in se1)
print('Oracle' in se1)
print('Python' not in se1)
print(100 not in se1)
print(20 in se1)
print(20 not in se1)

Solution 2:
'''
def set_membership():
    print('Parayana' in se1)
    print('Django' in se1)
    print('Oracle' in se1)
    print('Python' not in se1)
    print(100 not in se1)
    print(20 in se1)
    print(20 not in se1)
se1={10,20,30,True,100,'Parayana','Python'}
set_membership()