'''
Input
Remove duplicate elements from a list while preserving the original order.
Output:
Enter elements: 1 2 2 3 1 4 3
List without duplicates: ['1', '2', '3', '4']

s=input("Enter elements:").split()
li=[]
for i in s:
    if i not in li:
        li.append(i)
print("List without duplicates:",li)

Solution 2:
'''
def remove_element(s):
    li=[]
    for i in s:
        if i not in li:
            li.append(i)
    return li
s=input("Enter elements:").split()
print("List without duplicates:",remove_element(s))