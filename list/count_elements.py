'''
Input:
Count how many times an element appears.
Output:
Enter elements:apple banana apple cherry
Enter the word to count:apple
Count of apple is: 2

s=input("Enter elements:").split()
a=input("Enter the word to count:")
w=s.count(a)
print(f"Count of {a} is:",w)

Solution 2:
'''
def count_elements():
    w=s.count(a)
    return w
s=input("Enter elements:").split()
a=input("Enter the word to count:")
w=count_elements()
print(f"Count of {a} is:",w)
