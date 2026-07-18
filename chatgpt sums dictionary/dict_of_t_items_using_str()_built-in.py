'''
Input:
Create a dictionary with five items and print its Equivalent Strings.
Output:
85
Equivalent string:{'Name': 'Sagar', 'Age': 20, 'Place': 'Gutur', 'Study': 'B.Tech', 'College': 'VVITU'}

d1={"Name":"Sagar","Age":20,"Place":"Gutur","Study":"B.Tech","College":"VVITU"}
st=str(d1)
print(len(st))
print("Equivalent string:%s"%st)

Solution 2:
'''
def str_fun():
    st=str(d1)
    print(len(st))
    print("Equivalent string:%s"%st)
d1={"Name":"Sagar","Age":20,"Place":"Gutur","Study":"B.Tech","College":"VVITU"}
str_fun()