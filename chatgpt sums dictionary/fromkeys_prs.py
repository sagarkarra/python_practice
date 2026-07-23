'''
Input:
Create
["Python","Java","C"] as dictionary keys with value 100.
Create
["A","B","C","D"] using fromkeys() without giving a value.
Output:
New dictionary: {'Java': 100, 'Python': 100, 'C': 100}
New dictionary: {'A': None, 'D': None, 'C': None, 'B': None}

s={"Python","Java","C"}
d=dict.fromkeys(s,100)
print("New dictionary: %s" %str(d))

x={"A","B","C","D"}
q=dict.fromkeys(x)
print("New dictionary: %s" %str(q))

Solution 2:
'''
def fromkeys_prs():
    d=dict.fromkeys(s,100)
    print("New dictionary: %s" %str(d))
    q=dict.fromkeys(x)
    print("New dictionary: %s" %str(q))
s={"Python","Java","C"}
x={"A","B","C","D"}
fromkeys_prs()