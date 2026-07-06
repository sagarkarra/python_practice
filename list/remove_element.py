'''
Input:
Remove a specific element from a list.
Output:
Enter elements:sagar is a good boy
Enter the element to remove:good
After removing specific element is: ['sagar', 'is', 'a', 'boy']

s=input("Enter elements:").split()
word=input("Enter the element to remove:")
s.remove(word)
print("After removing specific element is:",s)

Solution 2:
'''
def remove_element():
    s.remove(word)
    return s
s=input("Enter elements:").split()
word=input("Enter the element to remove:")
res=remove_element()
print("After removing specific element is:",res)