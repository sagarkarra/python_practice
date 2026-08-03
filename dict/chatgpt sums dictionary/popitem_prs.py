'''
Input:
Create a dictionary with four items.
Call popitem() twice.
Print the dictionary after each call.
Output:
{'id': 101, 'name': 'Ravi', 'age': 20, 'city': 'Hyderabad'}
{'id': 101, 'name': 'Ravi', 'age': 20}
{'id': 101, 'name': 'Ravi'}

student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
print(student)
student.popitem()
print(student)
student.popitem()
print(student)

Solution 2:
'''
def popitem_prs():
    print(student)
    student.popitem()
    print(student)
    student.popitem()
    print(student)
student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
popitem_prs()