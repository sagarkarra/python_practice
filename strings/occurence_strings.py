'''
Input:
s = "banana"

Output:
Enter a string:Kalyani
Enter the char you want to count:a
Occurecnce of characters: 2

Find how many times 'a' occurs.
'''
s=input("Enter a string:")
count=0
str=input("Enter the char you want to count:")
for i in s:
    if i in str:
        count+=1
print("Occurecnce of characters:",count)
'''
Solution :2
'''