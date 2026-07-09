'''
Input:
Copy a list without affecting the original.
Output:
Enter strings:1 2 3
Enter element to s:4
Output of s is ['1', '2', '3']
Output of r is ['1', '2', '3', '4']

s=input("Enter strings:").split()
w=s.copy()
r=input("Enter element to s:")
w.append(r)
print("Output of s is",s)
print("Output of r is",w)

Solution 2:
'''
def copy_list():
    w=s.copy()
    w.append(r)
    print("Output of s is",s)
    print("Output of r is",w)
s=input("Enter strings:").split()
r=input("Enter element to s:")
copy_list()