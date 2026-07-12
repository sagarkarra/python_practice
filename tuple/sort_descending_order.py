'''
Input:
Given a tuple of (name, score) pairs, sort it by score in descending order.
Output:
Enter number of students:3
Enter name:Sagar
Enter score:85
Enter name:Theresa
Enter score:90
Enter name:Jyothsna
Enter score:95
Sorted record of name and score is: [(95, 'Jyothsna'), (90, 'Theresa'), (85, 'Sagar')]

n=int(input("Enter number of students:"))
li=[]
for i in range(n):
    name=input("Enter name:")
    score=int(input("Enter score:"))
    li.append((score,name))
li.sort(reverse=True)
print("Sorted record of name and score is:",li)

Solution 2:
'''
def sort_descending_order():
    li=[]
    for i in range(n):
        name=input("Enter name:")
        score=int(input("Enter score:"))
        li.append((score,name))
    li.sort(reverse=True)
    print("Sorted record of name and score is:",li)
n=int(input("Enter number of students:"))
sort_descending_order()
