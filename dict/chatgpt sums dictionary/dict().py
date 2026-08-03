'''
Input:
Membership operators checking
Output:
{'name': 'Sagar', 'age': 20, 'city': 'Guntur', 'Engineering': 'B.Tech', 'College': 'VVITU', 'Branch': 'CAD'}
Name is: Sagar
Age is: 20
City Name is: Guntur
Engineering is: B.Tech
College Name is: VVITU
Branch Name is: CAD
True
False
False
True
True
False
True
False
True
False
True
False
True
False

details={"name":"Sagar","age":20,"city":"Guntur","Engineering":"B.Tech","College":"VVITU","Branch":
         "CAD"}
print(details)
print("Name is:",details["name"])
print("Age is:",details["age"])
print("City Name is:",details["city"])
print("Engineering is:",details["Engineering"])
print("College Name is:",details["College"])
print("Branch Name is:",details["Branch"])
print("name" in details)
print("name" not in details)
print("address" in details)
print("address" not in details)
print("age" in details)
print("age" not in details)
print("city" in details)
print("city" not in details)
print("Engineering" in details)
print("Engineering" not in details)
print("College" in details)
print("College" not in details)
print("Branch" in details)
print("Branch" not in details)

Solution 2:
'''
def dict():
    print(details)
    print("Name is:",details["name"])
    print("Age is:",details["age"])
    print("City Name is:",details["city"])
    print("Engineering is:",details["Engineering"])
    print("College Name is:",details["College"])
    print("Branch Name is:",details["Branch"])
    print("name" in details)
    print("name" not in details)
    print("address" in details)
    print("address" not in details)
    print("age" in details)
    print("age" not in details)
    print("city" in details)
    print("city" not in details)
    print("Engineering" in details)
    print("Engineering" not in details)
    print("College" in details)
    print("College" not in details)
    print("Branch" in details)
    print("Branch" not in details)
details={"name":"Sagar","age":20,"city":"Guntur","Engineering":"B.Tech","College":"VVITU","Branch":
         "CAD"}
dict()