'''
Input:
Create a copy of a dictionary.Modify the copied dictionary.Check whether the original changes.
Output:
Original Dictionary: {'name': 'Ravi', 'age': 20, 'city': 'Hyderabad'}
Copied Dictionary: {'name': 'Ravi', 'age': 21, 'city': 'Vijayawada'}

d1 = {"name": "Ravi","age": 20,"city": "Hyderabad"}
d2 = d1.copy()
d2["age"] = 21
d2["city"] = "Vijayawada"
print("Original Dictionary:", d1)
print("Copied Dictionary:", d2)

Solution 2:
'''
def copy_prs():
    d2 = d1.copy()
    d2["age"] = 21
    d2["city"] = "Vijayawada"
    print("Original Dictionary:", d1)
    print("Copied Dictionary:", d2)
d1 = {"name": "Ravi","age": 20,"city": "Hyderabad"}
