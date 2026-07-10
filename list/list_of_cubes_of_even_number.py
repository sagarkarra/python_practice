'''
Input:
Create a list of cubes of even numbers from 1 to 20.
Output:
Cubes of even numbers from 1 to 20:
[8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

cubes=[i**3 for i in range(1, 21) if i%2==0]
print("Cubes of even numbers from 1 to 20:")
print(cubes)

Solution 2:
'''
def cubes_of_even_numbers():
    cubes=[i**3 for i in range(1, 21) if i%2==0]
    print("Cubes of even numbers from 1 to 20:")
    print(cubes)
cubes_of_even_numbers()