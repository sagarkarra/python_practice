'''
Input:
Reverse a list without using reverse().
Output:
Enter elements:apple banana cherry
After reversing the list: ['cherry', 'banana', 'apple']

s=input("Enter elements:").split()
res=s[::-1]
print("After reversing the list:",res)

Solution 2:
'''
def reverse_function():
    res=s[::-1]
    return res
s=input("Enter elements:").split()
w=reverse_function()
print("After reversing the list:",w)