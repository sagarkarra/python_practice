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
def membership(set1,val1):
    if val1 in set1:
        return "Found"
    else:
        return "Not found"
set1={10, 20, 30, 40}
val1=20
output1=membership(set1,val1)
print(output1)
set2={"Python", "C", "C++"}
val2="Java"
output2=membership(set2,val2)
print(output2)
set3={60, 70, 80, 90}
val3=50
output3=membership(set3,val3)
print(output3)