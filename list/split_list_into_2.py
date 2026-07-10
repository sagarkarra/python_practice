'''
Input:
Split a list into two equal halves.
Output:
Enter the elements:1 2 3 4 5 6
First half: ['1', '2', '3']
Second half: ['4', '5', '6']

s = input("Enter the elements:").split()
mid=len(s)//2
first_half=s[:mid]
second_half=s[mid:]
print("First half:", first_half)
print("Second half:", second_half)

Solution 2:
'''
def split_list(s):
    mid=len(s)//2
    first_half=s[:mid]
    second_half=s[mid:]
    print("First half:", first_half)
    print("Second half:", second_half)
s = input("Enter the elements:").split()
split_list(s)