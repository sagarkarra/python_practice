'''
Task: Tuples are immutable, but we can bypass this by transforming them. Write a program that takes a
tuple of integers, squares each number, and returns the final updated values as a tuple.
Sample Input: (2, 4, 6)
Expected Output: (4, 16, 36)

s=eval(input("Sample Input: "))
y=tuple([i**2 for i in s])
print("Expected Output: ",y)

Solution 2:
'''
def unpacking_modifying():
    y=tuple([i**2 for i in s])
    print("Expected Output: ",y)
s=eval(input("Sample Input: "))
unpacking_modifying()