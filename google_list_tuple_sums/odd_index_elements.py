'''
Input:
Write a program that takes a list of integers and returns a new list containing only the elements
located at odd indices
Output:
Enter integers:10 20 30 40 50 60
[10, 20, 30, 40, 50, 60]
Odd Index elements are: [20, 40, 60]

li=[]
for x in input("Enter integers:").split():
    li.append(int(x))
print(li)
odd_index=li[1::2]
print("Odd Index elements are:",odd_index)

Solution 2:
'''
def odd_index():
    li=[]
    for x in input("Enter integers:").split():
        li.append(int(x))
    print(li)
    odd_index=li[1::2]
    print("Odd Index elements are:",odd_index)
odd_index()