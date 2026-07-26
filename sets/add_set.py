'''
Input:
Write a program to add a element to the existing using add(element) or Add()
Output:
{'yellow', 'red'}
{1, 2, 3, 4, 5}
<class 'set'>
{1, 2, 3, 4, 5, 6, 7}

colours={"red","yellow"}
colours.add("yellow")
print(colours)
print()
se1={1,2,3,4,5}
print(se1)
print(type(se1))
se1.add(6)
se1.add(7)
print(se1)

Solution 2:
'''
def add_set():
    colours={"red","yellow"}
    colours.add("yellow")
    print(colours)
    print()
    se1={1,2,3,4,5}
    print(se1)
    print(type(se1))
    se1.add(6)
    se1.add(7)
    print(se1)
add_set()
