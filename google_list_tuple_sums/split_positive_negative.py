'''
Task: Given a list of numbers, compute and print the sum of all positive numbers and the product of all
negative numbers separately.
Sample Input: [4, -2, 5, -3, 2]
Expected Output: 
Positive Sum: 11, 
Negative Product: 6

s=eval(input("Sample Input: "))
sum=0
product=1
for i in s:
    if i>0:
        sum+=i
    else:
        product*=i
print("Positive Sum: ",sum)
print("Negative Product: ",product)

Solution 2:
'''
def split_pos_neg():
    t=0
    pr=1
    for i in s:
        if i>0:
            t+=i
        else:
            pr*=i
    print("Positive Sum: ",t)
    print("Negative Product: ",pr)
s=eval(input("Sample Input: "))
split_pos_neg()
