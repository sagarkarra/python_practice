'''
Input:
Convert a list to a tuple and vice versa.
Output:
Enter elements:1 2 3 4 5
List to tuple is: ('1', '2', '3', '4', '5')
Tuple to list is: ['1', '2', '3', '4', '5']

s=input("Enter elements:").split()
t=tuple(s)
print("List to tuple is:",t)
u=list(t)
print("Tuple to list is:",u)

Solution 2:
'''
def list_to_tuple():
    t=tuple(s)
    print("List to tuple is:",t)
    u=list(t)
    print("Tuple to list is:",u)
s=input("Enter elements:").split()
list_to_tuple()