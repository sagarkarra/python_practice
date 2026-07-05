'''
Input:
Print1 the first, last, and middle elements of a list.
Output:
Enter the values:10 20 30 40 50 60
First element is 10
Middle element is 40
Last element is 60

values=input("Enter the values:").split()
print("First element is",values[0])
print("Middle element is",values[len(values)//2])
print("Last element is",values[-1])

Solution 2:
'''
def print_elements(values):
    print("First element:", values[0])
    print("Middle element:", values[len(values) // 2])
    print("Last element:", values[-1])

numbers =input("Enter the values:").split()
print_elements(numbers)

