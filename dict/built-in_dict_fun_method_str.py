'''
Input:
Write a program to print the equivalent string of a dictionary.
Output:
46
Equivalent string: {'Name': 'Sagar', 'Age': 20, 'Class': 'First'}

d1={"Name":"Sagar","Age":20,"Class":"First"}
st=str(d1)
print(len(st))
print("Equivalent string: %s" %st)

Solution 2:
'''
def str_fun():
    st=str(d1)
    print(len(st))
    print("Equivalent string: %s" %st)
d1={"Name":"Sagar","Age":20,"Class":"First"}
str_fun()