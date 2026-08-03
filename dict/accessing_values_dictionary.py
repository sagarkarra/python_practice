'''
Input:
Write a program to access the values in a dictionary 
Output:
Id Number is 100
Name is Sagar
Subjects are: ['SQL Server', 'Oracle', 'Python']
First subject name is SQL Server
Second subject name is Oracle
Third subject name is Python

s={'Id':100,'Name':'Sagar','Subjects':["SQL Server","Oracle","Python"]}
print("Id Number is",s['Id'])
print("Name is",s['Name'])
print("Subjects are:",s["Subjects"])
print("First subject name is",s['Subjects'][0])
print("Second subject name is",s['Subjects'][1])
print("Third subject name is",s['Subjects'][2])

Solution 2:
'''
def access_values():
    print("Id Number is",s['Id'])
    print("Name is",s['Name'])
    print("Subjects are:",s["Subjects"])
    print("First subject name is",s['Subjects'][0])
    print("Second subject name is",s['Subjects'][1])
    print("Third subject name is",s['Subjects'][2])
s={'Id':100,'Name':'Sagar','Subjects':["SQL Server","Oracle","Python"]}
access_values()
