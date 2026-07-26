'''
Input:
Create a set of city names and remove all elements using clear().
Print the set before and after using clear().
Output:
Before clear() method: {'hyderabad', 'guntur', 'vijayawada'}
After clear() method: set()

cities={"guntur","vijayawada","hyderabad"}
print("Before clear() method:",cities)
cities.clear()
print("After clear() method:",cities)

Solution 2:
'''
def clear_set_prs():
    print("Before clear() method:",cities)
    cities.clear()
    print("After clear() method:",cities)
cities={"guntur","vijayawada","hyderabad"}
clear_set_prs()