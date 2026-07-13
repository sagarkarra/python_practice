'''
Task: Write a program to extract the middle 4 elements of a 8-element tuple,
reverse them, and print the resulting sub-tuple.
Sample Input:(1, 2, 3, 4, 5, 6, 7, 8)
Expected Output: (6, 5, 4, 3)

t = eval(input("Sample Input:"))
print("Expected Output:",t[5:1:-1])

Solution 2:
'''
def ext_mid():
    print("Expected Output:",t[5:1:-1])
t = eval(input("Sample Input:"))
ext_mid()