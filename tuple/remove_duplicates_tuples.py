'''
Input:
Remove duplicate elements from a tuple while preserving their original order.
Output:
Enter elements:1 2 2 3 1 4 3
tuple without duplicates: ('1', '2', '3', '4')

s=tuple(input("Enter elements:").split())
li=[]
for i in s:
    if i not in li:
        li.append(i)
t=tuple(li)
print("tuple without duplicates:",t)

Solution 2:
'''
def remove_element(s):
    li=[]
    for i in s:
        if i not in li:
            li.append(i)
    t=tuple(li)
    return t
s=tuple(input("Enter elements:").split())
print("Tuple without duplicates:",remove_element(s))