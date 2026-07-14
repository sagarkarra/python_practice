'''
Task: Write a program to find the maximum and minimum numbers in a given tuple without using the built-
in max() or min() functions.
Sample Input: (23, 67, 12, 89, 45)
Expected Output: Min: 12, Max: 89

s=eval(input("Sample Input: "))
min=s[0]
max=s[0]
for i in s:
    if i<min:
        min=i
    elif i>max:
        max=i
print(f"Expected Output: Min: {min}, Max: {max}")

Solution 2:
'''
def tuple_minmax():
    min=s[0]
    max=s[0]
    for i in s:
        if i<min:
            min=i
        elif i>max:
            max=i
    print(f"Expected Output: Min: {min}, Max: {max}")
s=eval(input("Sample Input: "))
tuple_minmax()