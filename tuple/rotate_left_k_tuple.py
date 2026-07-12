'''
Input:
Rotate a tuple to the left by k positions.
Output:
Enter tuple elements:1 2 3 4 5
Enter k:2
Left-rotated tuple: ('3', '4', '5', '1', '2')

t=tuple(input("Enter tuple elements:").split())
k=int(input("Enter k:"))
k%=len(t)
r=t[k:]+t[:k]
print("Left-rotated tuple:",r)

Solution 2:
'''
def rotate_tuple_by_k_to_lift():
    k=int(input("Enter k:"))
    k%=len(t)
    r=t[k:]+t[:k]
    print("Left-rotated tuple:",r)  
t=tuple(input("Enter tuple elements:").split())
rotate_tuple_by_k_to_lift()