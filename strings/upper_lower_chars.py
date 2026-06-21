'''
Input:
s = "Hello World"
Output:
Lowercase is sagar karra
Uppercase is SAGAR KARRA
Convert the entire string to lowercase,uppercase.

s=input("Enter the string:")
print("Lowercase is",s.lower())
print("Uppercase is",s.upper())
'''
def upper_lower(s):
    uppers=s.upper()
    lowers=s.lower()
    return uppers,lowers
s=input("Enter the string:")
uppers,lowers=upper_lower(s)
print("Lowercase is",lowers)
print("Uppercase is",uppers)
