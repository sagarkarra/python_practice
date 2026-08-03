'''
Input:
Print all keys using keys().
Print each key using a for loop.
Create the following dictionary:
student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
Output:
dict_keys(['id', 'name', 'age', 'city'])
id
name
age
city

student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
k=student.keys()
print(k)
for k in student.keys():
    print(k)

Solution 2:
'''
def dict_keys_prs():
    k=student.keys()
    print(k)
    for k in student.keys():
        print(k)
student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
dict_keys_prs()