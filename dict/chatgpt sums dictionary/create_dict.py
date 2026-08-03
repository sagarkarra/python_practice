'''
Input:
Create an empty dictionary called student.
Add the following key-value pairs to the dictionary:
"id" → 101
"name" → "Ravi"
"age" → 20
Output:
{}
<class 'dict'>
{'id': 101, 'name': 'Ravi', 'Age': 20}
<class 'dict'>
Print the dictionary.

student={}
print(student)
print(type(student))
student["id"]=101
student["name"]="Ravi"
student["Age"]=20
print(student)
print(type(student))

Solution 2:
'''
def create_dict():
    student={}
    print(student)
    print(type(student))
    student["id"]=101
    student["name"]="Ravi"
    student["Age"]=20
    print(student)
    print(type(student))
create_dict()