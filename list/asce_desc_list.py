'''
Input:
Sort a list in ascending and descending order.
Output:
Enter elements:10 50 30 40 20
List in ascending order is: ['10', '20', '30', '40', '50']
List in descending order is: ['50', '40', '30', '20', '10']

s=input("Enter elements:").split()
s.sort()
print("List in ascending order is:",s)
s.sort(reverse=True)
print("List in descending order is:",s)

Solution 2:
'''
def asce_desc(s):
    s.sort()
    print("List in ascending order is:",s)
    s.sort(reverse=True)
    print("List in descending order is:",s)
s=input("Enter elements:").split()
asce_desc(s)
