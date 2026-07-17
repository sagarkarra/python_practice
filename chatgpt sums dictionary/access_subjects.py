'''
Given
student={"name":"Sai","subjects":["Python","SQL","Java"]}
Print:
first subject
second subject
third subject
Output:
First subject is: Python
Second subject is: SQL
Third subject is: Java

student={"name":"Sai","subjects":["Python","SQL","Java"]}
print("First subject is:",student["subjects"][0])
print("Second subject is:",student["subjects"][1])
print("Third subject is:",student["subjects"][2])

Solution 2:
'''
def access_subjects():
    print("First subject is:",student["subjects"][0])
    print("Second subject is:",student["subjects"][1])
    print("Third subject is:",student["subjects"][2])
student={"name":"Sai","subjects":["Python","SQL","Java"]}
access_subjects()