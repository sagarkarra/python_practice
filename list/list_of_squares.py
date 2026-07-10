'''
Input:
Create a list of squares from 1 to 20.
Output:
Squares from 1 to 20:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

y=[x*x for x in range(1,21)]
print("Squares from 1 to 20:")
print(y)

Solution 2:
'''
def list_squares():
    y=[x*x for x in range(1,21)]
    print("Squares from 1 to 20:")
    print(y)
list_squares()