'''
Input:
Check whether a tuple is a palindrome.
Output:
Enter string:mam
('m', 'a', 'm')
Tuple is palindrome

s=tuple(input("Enter string:"))
print(s)
if s==s[::-1]:
    print("Tuple is palindrome")
else:
    print("Tuple is not palindrome")

Solution 2:
'''
def tuple_palindrome():
    if s==s[::-1]:
        print("Tuple is palindrome")
    else:
        print("Tuple is not palindrome")
s=tuple(input("Enter string:"))
tuple_palindrome()