'''
Input:
Rotate a list by k positions.
Output:
Enter the elements:1 2 3 4 5
Enter the number of positions to rotate: 2
Rotated list: ['4', '5', '1', '2', '3']

s = input("Enter the elements:").split()
k = int(input("Enter the number of positions to rotate: "))
if s:
    k %= len(s)
    lst = s[-k:] + s[:-k]
print("Rotated list:", lst)

Solution 2
'''
def rotate_by_k(s,k):
    if not s:
        return s
        k %= len(s)
    lst = s[-k:] + s[:-k]
    return lst
s = input("Enter the elements:").split()
k = int(input("Enter the number of positions to rotate: "))
res=rotate_by_k(s,k)
print("Rotated list:", res)