'''
Input:
Copy the set:{"red", "green", "blue"} into another variable.
Add "yellow" to the copied set.
Check whether the original set changes.

s={"red", "green", "blue"}
x=s.copy()
x.add("yellow")
print(s)
print(x)
if x == s:
    print("Set changed")
else:
    print("Set not changed")

Solution 2:
'''
def copy_set():
    x=s.copy()
    x.add("yellow")
    print(s)
    print(x)
    if x == s:
        print("Set changed")
    else:
        print("Set not changed")
s={"red", "green", "blue"}
copy_set_prs()