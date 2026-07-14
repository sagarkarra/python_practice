'''
Task: Write a program that removes all duplicate values from a list while keeping the original order of
the remaining items intact.
Sample Input: ['apple', 'banana', 'apple', 'cherry', 'banana']
Expected Output: ['apple', 'banana', 'cherry']

s=eval(input("Sample Input: "))
li=[]
for i in s:
    if i not in li:
        li.append(i)
print("Expected Output: ",li)

Solution 2:
'''
def remove_duplicates():
    li=[]
    for i in s:
        if i not in li:
            li.append(i)
    print("Expected Output: ",li)
s=eval(input("Sample Input: "))
remove_duplicates()