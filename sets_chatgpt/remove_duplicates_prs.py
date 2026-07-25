'''
Input:
Remove duplicate values from:
[10, 20, 20, 30, 40, 40, 50]
Output:
[40, 10, 50, 20, 30]
<class 'list'>

s=[10, 20, 20, 30, 40, 40, 50]
s=list(set(s))
print(s)
print(type(s))

Solution 2:
'''
def remove_duplicates_prs():
    s=[10, 20, 20, 30, 40, 40, 50]
    s=list(set(s))
    print(s)
    print(type(s))
remove_duplicates_prs()