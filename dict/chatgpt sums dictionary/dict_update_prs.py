'''
Input:
Merge
d1={"a":10,"b":20}
d2={"c":30,"d":40}
Update the value of "b" to 100 using update().

d1={"a":10,"b":20}
d2={"c":30,"d":40}
d1.update(d2)
print(d1)
d1={"a":10,"b":100}
d2={"c":30,"d":40}
d1.update(d2)
print(d1)

Solution 2:
'''
def dict_update_prs():
    d1 = {"a":10, "b":20}
    d2 = {"c":30, "d":40}
    d1.update(d2)
    print(d1)
    d1 = {"a":10, "b":100}
    d2 = {"c":30, "d":40}
    d1.update(d2)
    print(d1)
dict_update_prs()