'''
Input:
Reverse a tuple without using reversed().
Output:
Enter elements:1 2 3 4 5
Original tuple is: ('1', '2', '3', '4', '5')
After reversing a tuple: ('5', '4', '3', '2', '1')

s = tuple(input("Enter elements:").split())
print("Original tuple is:",s)
rev = tuple(reversed(s))
print("After reversing a tuple:", rev)

Solution 2:
'''
def reverse_tuple():
    print("Original tuple is:",s)
    rev = tuple(reversed(s))
    print("After reversing a tuple:", rev)
s = tuple(input("Enter elements:").split())
reverse_tuple()