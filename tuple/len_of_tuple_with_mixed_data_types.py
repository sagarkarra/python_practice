'''
Input:
Find the length of a tuple containing mixed data types.
Output:
Enter an integer:10 
Enter True or False:True
Enter a string:Sagar
Enter a decimal number:10.5
(10,True,'Sagar',10.5)
Length:4

t=(int(input("Enter an integer:")),
   bool(input("Enter True or False:")=="True"),
   input("Enter a string:"),
   float(input("Enter a decimal number:"))
)
print(t)
print("Length:",len(t))

Solution 2:
'''
def len_tuple_with_mixed_data_tuple():
    length=len(t)
t=(int(input("Enter an integer:")),
   bool(input("Enter True or False:")=="True"),
   input("Enter a string:"),
   float(input("Enter a decimal number:")))
print(t)
print("Length:",len(t))
len_tuple_with_mixed_data_tuple()