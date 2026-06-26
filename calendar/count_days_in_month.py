'''
Input:
Count Days in a Month

Output:
Enter year:2026
Enter month:6
Days in month is: 30

Input a year and month.
Find how many days are in that month

import calendar as c
year=int(input("Enter year:"))
month=int(input("Enter month:"))
days=c.monthrange(year,month)[1]
print("Days in month is:",days)

Solution 2:
'''
import calendar as c
def count_days(year,month):
    days=c.monthrange(30)
    return days
year=int(input("Enter year:"))
month=int(input("Enter month:"))
days=c.monthrange(year,month)[1]
print("Days in month is:",days)