'''
Input:
Find the maximum and minimum values in a list.
Output:
Enter elements:10 20 30 40 50
Max element is: 50
Min element is: 10

s=input("Enter elements:").split()
max_value=max(s)
min_value=min(s)
print("Max element is:",max_value)
print("Min element is:",min_value)

Solution 2:
'''
def max_min_element(s):
    max_value=max(s)
    min_value=min(s)
    print("Max element is:",max_value)
    print("Min element is:",min_value)
s=input("Enter elements:").split()
max_min_element(s)