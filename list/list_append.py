'''
Input:
Add an element to the end of a list.
Output:
Enter values:10 20 30 40 
Enter the value to append:50
After appending the number ['10', '20', '30', '40', '50']


values=input("Enter values:").split()
number=input("Enter the value to append:")
values.append(number)
print("After appending the number",values)

Solution 2:
'''
def append_element(values, number):
    values.append(number)
    return values
values = input("Enter values:").split()
number = input("Enter the value to append:")
result = append_element(values, number)
print("After appending the number", result)