'''
Input:
student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
Print all key-value pairs.
{'id': 101, 'name': 'Ravi', 'age': 20, 'city': 'Hyderabad'}
dict_items([('id', 101), ('name', 'Ravi'), ('age', 20), ('city', 'Hyderabad')])
('id', 101)
('name', 'Ravi')
('age', 20)
('city', 'Hyderabad')

student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
print(student)
dit=student.items()
print(dit)
for its in dit:
    print(its)

Solution 2:
'''
def dict_items_prs():
    print(student)
    dit=student.items()
    print(dit)
    for its in dit:
        print(its)
student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
dict_items_prs()