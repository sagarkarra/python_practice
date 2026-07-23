'''
Input:
Create the following dictionary:
student = {"id": 101,"name": "Ravi","age": 20}
Use the get() method to print the value of the "name" key.
Use the get() method to print the value of the "city" key, which does not exist.
Use the get() method to print the value of the "city" key. If the key is not present, display 
"Not Found"
Output:
Name: Ravi
City: NA
City: Not Found
'''
student = {"id": 101,"name": "Ravi","age": 20}
print("Name: %s" %student.get('name','Ravi'))
print("City: %s" %student.get('city','NA'))
print("City: %s" %student.get('city','Not Found'))