'''
Input:
Check whether 20 is present in:
{10, 20, 30, 40}
Check whether "Java" is not present in:
{"Python", "C", "C++"}
Write a program that prints "Found" if 50 is in the set; otherwise print "Not Found".
Output:
membership.py
True
True
Not found

se={10, 20, 30, 40}
print(20 in se)
s={"Python", "C", "C++"}
print("Java" not in s)
se={10,20,30,40}
if 50 in se:
    print("Found")
else:
    print("Not found")

Solution 2:
'''
def memebership_prs():
    se={10, 20, 30, 40}
    print(20 in se)
    s={"Python", "C", "C++"}
    print("Java" not in s)
    se={10,20,30,40}
    if 50 in se:
        print("Found")
    else:
        print("Not found")
memebership_prs()