'''
Input:
When you call this function with respect to empty dictionary then we get None as result.For example:
d1={10:1.2,20:3.4,30:1.2,40:4.5,50:3.4}
print(d1.clear())
print({}.clear())
print(dict().clear())
Output:
None
None
None

Example:
d={'Name':"Vani",'Age':7}
print("Start len:%d" %len(d))
d.clear()
print("End len:%d" %len(d))
Output:
Start len:2
End len:0


d={'Name':"Vani",'Age':7}
print("Start len:%d" %len(d))
d.clear()
print("End len:%d" %len(d))

Solution 2:
'''
def none_Result():
    print("Start len:%d" %len(d))
    d.clear()
    print("End len:%d" %len(d))
d={'Name':"Vani",'Age':7}
none_Result()