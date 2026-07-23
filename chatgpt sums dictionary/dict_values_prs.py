'''
Input:
Print all values using values().
Print each value using a for loop.
student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
Output:
dict_values([101, 'Ravi', 20, 'Hyderabad'])
101
Ravi
20
Hyderabad

student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
vs=student.values()
print(vs)
for v in vs:
    print(v)
'''
def dict_values_prs():
    vs=student.values()
    print(vs)
    for v in vs:
        print(v)
student = {"id": 101,"name": "Ravi","age": 20,"city": "Hyderabad"}
