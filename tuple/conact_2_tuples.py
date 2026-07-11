'''
Input:
Concatenate two tuples and display the result.
Output:
Enter values of t1:10 20 30
Enter values of t2:40 50 60
Final tuple is: ['10', '20', '30', '40', '50', '60']

t1=input("Enter values of t1:").split()
t2=input("Enter values of t2:").split()
t3=t1+t2
print("Final tuple is:",t3)

Solution 2:
'''
def concat_2_tuples():
    t3=t1+t2
    print("Final tuple is:",t3)
t1=input("Enter values of t1:").split()
t2=input("Enter values of t2:").split()
concat_2_tuples()