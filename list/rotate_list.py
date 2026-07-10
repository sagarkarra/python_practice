'''
Input:
Rotate a list by one position to the right.
Output:
Enter the elements: 1 2 3 4 5
Rotated list: ['5', '1', '2', '3', '4']

s = input("Enter the elements: ").split()
if s:
    s.insert(0, s.pop())

print("Rotated list:", s)

Solution 2:
'''
def rotate_list(s):
    if s:
        s.insert(0, s.pop())
    return s

s = input("Enter the elements: ").split()

print("Rotated list:", rotate_list(s))
