'''
Input:
Remove the last element using pop().
Output:
Enter the elements:10 20 30 40 50
Removed element: 50
Updated list: ['10', '20', '30', '40']

numbers = input("Enter the elements:").split()
removed = numbers.pop()
print("Removed element:", removed)
print("Updated list:", numbers)

Solution 2:
'''
def remove_last(lst):
    removed = lst.pop()
    print("Removed element:", removed)
    print("Updated list:", lst)
numbers = input("Enter the elements:").split()
remove_last(numbers)