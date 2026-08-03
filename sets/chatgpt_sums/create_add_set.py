'''
Input:
Create a set {10, 20, 30} and add 40.
Add "orange" to the set:
{"apple", "banana"}
Add 100 to an empty set.
Output:
{10, 20, 30}
{40, 10, 20, 30}
{'banana', 'apple'}
{'banana', 'apple', 'orange'}
{100}

s={10, 20, 30}
print(s)
s.add(40)
print(s)
fru={"apple", "banana"}
print(fru)
fru.add("orange")
print(fru)
se=set()
se.add(100)
print(se)

Solution 2:
'''
def add_set():
    s={10, 20, 30}
    print(s)
    s.add(40)
    print(s)
    fru={"apple", "banana"}
    print(fru)
    fru.add("orange")
    print(fru)
    se=set()
    se.add(100)
    print(se)
add_set_prs()