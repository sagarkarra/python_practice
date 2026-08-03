'''
Input:
Write a program to check whether the value is present in dict or not
Output:
{'Id': 100, 'Name': 'Sagar', 'Location': 'Guntur', 'sal': 20000, 'commission': 200, 'company': 'Infosys'}
<class 'dict'>
1621506752576
True
True
False
True
True
False

s={'Id':100,'Name':'Sagar','Location':'Guntur','sal':20000,'commission':200,"company":"Infosys"}
print(s)
print(type(s))
print(id(s))
print("Id" in s)
print("Name" in s)
print("name" in  s)
print("fname" not in s)
print("sal" in s)
print("Company" in s)

Solution 2:
'''
def another():
    print(s)
    print(type(s))
    print(id(s))
    print("Id" in s)
    print("Name" in s)
    print("name" in  s)
    print("fname" not in s)
    print("sal" in s)
    print("Company" in s)
s={'Id':100,'Name':'Sagar','Location':'Guntur','sal':20000,'commission':200,"company":"Infosys"}
another()