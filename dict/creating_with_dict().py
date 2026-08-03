'''
Input:
Write a program to create a dictionary with dict() function
Output:
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
<class 'dict'>

d1=dict([("a",10),("b",20),("c",30),("d",40)])
print(d1)
print(type(d1))

Solution 2:
'''
def create_dict():
    d1=dict([("a",10),("b",20),("c",30),("d",40)])
    print(d1)
    print(type(d1))
create_dict()