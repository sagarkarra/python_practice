'''
Input:
Given
emp = {"id":101,"name":"Ravi","salary":35000}
Print:
employee id
employee name
salary
Output:
Employee ID: 101
Employee Name: Ravi
Salary: 35000

emp = {"id":101,"name":"Ravi","salary":35000}
print("Employee ID:",emp["id"])
print("Employee Name:",emp["name"])
print("Salary:",emp["salary"])

Solution 2:
'''
def access_values_dict():
    print("Employee ID:",emp["id"])
    print("Employee Name:",emp["name"])
    print("Salary:",emp["salary"])
emp = {"id":101,"name":"Ravi","salary":35000}
access_values_dict()