'''
Input:
Find all even and odd numbers in a list.
Ouptut:
Enter the numbers:1 2 3 4 5 6
Even numbers:[2, 4, 6]
Odd numbers:[1, 3, 5]

li = []
for x in input("Enter the numbers:").split():
    li.append(int(x))
even = []
odd = []
for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)

Solution 2:
'''
def odd_even():
    li = []
    for x in input("Enter the numbers:").split():
        li.append(int(x))
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("Even numbers:", even)
    print("Odd numbers:", odd)
odd_even()