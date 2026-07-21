'''
Input:
Write a program to obtain the value by passing the value of key,then we get None as result.This should
be done by using dict.get() 
Output:
print(d['sex'])  KeyError: 'sex'

d={'Name':"Vani",'Age':27}
print(d['sex'])
print("Value: %s" %dict.get('Age'))
print("Value: %s" %dict.get('sex',"NA"))

Solution 2:
'''
def dict_get_prs():
    print(d['sex'])
    print("Value: %s" %dict.get('Age'))
    print("Value: %s" %dict.get('sex',"NA"))
d={'Name':"Vani",'Age':27}
dict_get_prs()
