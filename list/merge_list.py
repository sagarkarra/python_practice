'''
Input:
Merge two lists into one.
Output:
Enter strings of list 1:1 2 3
Enter strings of list 2:4 5 6
After merging 2 lists: ['1', '2', '3', '4', '5', '6']

s=input("Enter strings of list 1:").split()
r=input("Enter strings of list 2:").split()
w=s+r
print("After merging 2 lists:",w)

Solution 2:
'''
def merge_list():
    w=s+r
    print("After merging 2 lists:",w)
s=input("Enter strings of list 1:").split()
r=input("Enter strings of list 2:").split()
merge_list()