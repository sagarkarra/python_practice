'''
Input:
Remove duplicate characters from:"programming"
Output:
programming
<class 'str'>
{'r', 'n', 'a', 'g', 'm', 'p', 'i', 'o'}
rnagmpio
<class 'str'>

s='programming'
print(s)
print(type(s))
t=set(s)
print(t)
st="".join(t)
print(st)
print(type(st))

Solution 2:
'''
def another_prs():
    s='programming'
    print(s)
    print(type(s))
    t=set(s)
    print(t)
    st="".join(t)
    print(st)
    print(type(st))
another_prs()