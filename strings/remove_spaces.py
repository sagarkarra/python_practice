'''
Input:
s = "   Welcome   "
Output:
Enter a string:   Sagar   
After removing Spaces: Sagar
Remove spaces from both sides.

s=input("Enter a string:")
print("After removing Spaces:",s.strip())

Solution 2:
'''
def remove_space(s):
    string_space=s.strip()
    return string_space
s=input("Enter a string:")
string_space=remove_space(s)
print("After removing Spaces:",string_space)
