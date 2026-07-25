'''
Input:
Write a program to remove duplicate element from other sequence.
Output:
[40, 10, 20, 50]
<class 'list'>

lst=(10,20,10,40,50,10,20)
lst=list(set(lst))
print(lst)
print(type(lst))

Solution 2:
'''
def remove_duplicate_elements():
    lst=list(set(lst))
    print(lst)
    print(type(lst))
lst=(10,20,10,40,50,10,20)
remove_duplicate_elements()