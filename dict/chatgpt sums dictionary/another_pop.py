'''
Input:
Try removing a key that doesn't exist.
Observe the error.
emp = {"id":101,"name":"Ravi","salary":45000}
Output:
{'id': 101, 'name': 'Ravi', 'salary': 45000}
{'id': 101, 'name': 'Ravi'}
print(emp["salary"]) KeyError: 'salary'

emp = {"id":101,"name":"Ravi","salary":45000}
print(emp)
emp.pop("salary")
print(emp)
print(emp["salary"])

Solution 2:
'''
def another_pop():
    print(emp)
    emp.pop("salary")
    print(emp)
    print(emp["salary"])
emp = {"id":101,"name":"Ravi","salary":45000}
another_pop()