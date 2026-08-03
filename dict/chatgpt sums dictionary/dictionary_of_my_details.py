'''
Input:
Create a dictionary containing your own details and print every value separately.
Output:
{'name': 'Sagar', 'age': 20, 'city': 'Guntur', 'Engineering': 'B.Tech', 'College': 'VVITU', 'Branch': 'CAD', 'Courses': ['DSA', 'Java', 'DBMS', 'Advanced Python', 'Mathematics']}
Name is: Sagar
Age is: 20
City Name is: Guntur
Engineering is: B.Tech
College Name is: VVITU
Branch Name is: CAD
Courses are: ['DSA', 'Java', 'DBMS', 'Advanced Python', 'Mathematics']
1st Course Name is: DSA
2nd Course Name is: Java
3rd Course Name is: DBMS
4th Course Name is: Advanced Python
5th Course Name is: Mathematics

details={"name":"Sagar","age":20,"city":"Guntur","Engineering":"B.Tech","College":"VVITU","Branch":
         "CAD","Courses":["DSA","Java","DBMS","Advanced Python","Mathematics"]}
print(details)
print("Name is:",details["name"])
print("Age is:",details["age"])
print("City Name is:",details["city"])
print("Engineering is:",details["Engineering"])
print("College Name is:",details["College"])
print("Branch Name is:",details["Branch"])
print("Courses are:",details["Courses"])
print("1st Course Name is:",details["Courses"][0])
print("2nd Course Name is:",details["Courses"][1])
print("3rd Course Name is:",details["Courses"][2])
print("4th Course Name is:",details["Courses"][3])
print("5th Course Name is:",details["Courses"][4])

Solution 2:
'''
def dict_of_my_details():
    print(details)
    print("Name is:",details["name"])
    print("Age is:",details["age"])
    print("City Name is:",details["city"])
    print("Engineering is:",details["Engineering"])
    print("College Name is:",details["College"])
    print("Branch Name is:",details["Branch"])
    print("Courses are:",details["Courses"])
    print("1st Course Name is:",details["Courses"][0])
    print("2nd Course Name is:",details["Courses"][1])
    print("3rd Course Name is:",details["Courses"][2])
    print("4th Course Name is:",details["Courses"][3])
    print("5th Course Name is:",details["Courses"][4])
details={"name":"Sagar","age":20,"city":"Guntur","Engineering":"B.Tech","College":"VVITU","Branch":
         "CAD","Courses":["DSA","Java","DBMS","Advanced Python","Mathematics"]}
dict_of_my_details()