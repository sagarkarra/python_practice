'''
Input:
Find the second largest number in a list.
Output:
Enter the numbers:10 300 20 5000 40000
Second largest number: 5000

li = []
s=input("Enter the numbers:").split()
for i in s:
    li.append(int(i))
unique = []
for i in li:
    if i not in unique:
        unique.append(i)

if len(unique) < 2:
    print("There is no second largest number.")
else:
    unique.sort()
    print("Second largest number:", unique[-2])

Solution 2:
'''
def second_largest(li):
    unique = []
    for i in li:
        if i not in unique:
            unique.append(i)
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]
li = []
s=input("Enter the numbers:").split()
for i in s:
    li.append(int(i))
res = second_largest(li)
if res is None:
    print("There is no second largest number.")
else:
    print("Second largest number:", res)