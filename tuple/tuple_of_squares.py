'''
Input:
Create a tuple of squares of the numbers from 1 to n.
Output:
Enter a number:5
Square of Tuple values from 1 to 5:
(1, 4, 9, 16, 25)
'''
n=int(input("Enter a number:"))
y=[x*x for x in range(1,n+1)]
z=tuple(y)
print(f"Square of Tuple values from 1 to {n}:")
print(z)