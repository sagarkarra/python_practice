'''
Input:
Check whether a given element exists in a list.
Output:
Enter words:sagar is a boy
Element to check whether if exists:is
is is there in the word list

s=input("Enter words:").split()
word=input("Element to check whether if exists:")
if word in s:
    print(f"{word} is there in the word list")
else:
    print("No element in the list")

Solution 2:
'''
def check_element():
    if word in s:
        print(f"{word} is there in the word list")
    else:
        print("No element in the list")
s=input("Enter words:").split()
word=input("Element to check whether if exists:")
check_element()