'''
Input:
Check whether a given element exists in a tuple.
Output:
Enter words:sagar is a good boy
Element to check whether if exists:good
good is there in the word list
s = tuple(input("Enter elements:").split())
t = input("Enter the element to check:")

if t in s:
    print(f"{t} exists in the tuple")
else:
    print("Element does not exist in the tuple")

Solution 2:
'''
def check_element():
    if t in s:
        print(f"{t} is there in the word list")
    else:
        print("No element in the list")
s=tuple(input("Enter words:").split())
t=input("Element to check whether if exists:")
check_element()