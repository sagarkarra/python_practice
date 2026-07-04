'''Input:

s = "Python Programming"

Output:
Enter a string:Python Programming
Total characters: 18
Total words: 2

Find:

a)Total characters
b)Total words 
'''
s=input("Enter a string:")
print("Total characters:",len(s))
print("Total words:",len(s.split()))
'''
Solution 2:
'''
def total_char_words(str):
    total_char=len(s)
    total_words=len(s.split())
    return total_char,total_words
s=input("Enter a string:")
total_char,total_words=total_char_words
print("Total characters:",total_char)
print("Total words:",total_words)