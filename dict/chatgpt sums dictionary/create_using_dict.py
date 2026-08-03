'''
Input:
Create the same dictionary using dict().
{"a":10,"b":20,"c":30}
Output:
{'a': 10, 'b': 10, 'c': 10}
<class 'dict'>
3

s=dict([("a",10),("b",10),("c",10)])
print(s)
print(type(s))
print(len(s))
'''
def create_using_dict():
    s=dict([("a",10),("b",10),("c",10)])
    print(s)
    print(type(s))
    print(len(s))
create_using_dict()