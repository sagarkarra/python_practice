'''
Input:
s = "Python is easy to learn"
Output:
Enter a string:Sagar is a boy
Total words: 4
Total vowels: 5
Find:
a)Total words
b)Total vowels

s=input("Enter a string:")
words=s.split()
print("Total words:",len(words))
count=0
vowels=("a","e","i","o","u")
for i in s:
    if i in vowels:
        count+=1
print("Total vowels:",count)

Solution 2:
'''
def words_vowels(s):
    words=len(s.split())
    count=0
    vowels=("a","e","i","o","u")
    for i in s:
        if i in vowels:
            count+=1
    return words,count
s=input("Enter a string:")
words,count=words_vowels(s)
print("Total words:",words)
print("Total vowels:",count)