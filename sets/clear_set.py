'''
Input:
Write a program to create a set and clear the elements from a set.
Output:
Before clear(): {'guntur', 'hyderabad', 'vijayawada'}
After clear(): set()

cities={"guntur","vijayawada","hyderabad"}
print("Before clear():",cities)
cities.clear()
print("After clear():",cities)

Solution 2:
'''
def clear_set():
    print("Before clear():",cities)
    cities.clear()
    print("After clear():",cities)
cities={"guntur","vijayawada","hyderabad"}
clear_set()