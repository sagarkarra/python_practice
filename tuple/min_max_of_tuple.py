'''
Input:
Write a function that returns the maximum and minimum values of a tuple.
Output:
Enter elements:1 2 3 4 5 
('1', '2', '3', '4', '5')
Maximum element is 5
Minimum element is 1

s=tuple(input("Enter elements:").split())
print(s)
max_values=max(s)
print("Maximum element is",max_values)
min_values=min(s)
print("Minimum element is",min_values)
Solution 2:
'''
def min_max():
    print(s)
    max_values=max(s)
    print("Maximum element is",max_values)
    min_values=min(s)
    print("Minimum element is",min_values)
s=tuple(input("Enter elements:").split())
min_max()