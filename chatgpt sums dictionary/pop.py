'''
Input:
Remove "salary" from
emp = {"id":101,"name":"Ravi","salary":45000}
Output:
{'id': 101, 'name': 'Ravi', 'salary': 45000}
{'id': 101, 'name': 'Ravi'}

emp = {"id":101,"name":"Ravi","salary":45000}
print(emp)
emp.pop("salary")
print(emp)

Solution 2:
'''
def pop_prs():
    print(emp)
    emp.pop("salary")
    print(emp)
emp = {"id":101,"name":"Ravi","salary":45000}
pop_prs()