'''
Input:
Find the Weekday

Output:
Enter the year:2026
Enter the month:6
Enter the day: 26
The weekday is: Friday

Input a date (year, month, day).
Print the weekday name (Monday, Tuesday, etc.)

import calendar as c
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
day=int(input("Enter the day: "))

weekday=c.weekday(year,month,day)
weekday_name=c.day_name[weekday]
print("The weekday is:",weekday_name)

Solution 2:
'''
import calendar as c
def weekday_name(year,month,day):
    weekday=c.weekday(year,month,day)
    return c.day_name[weekday]
year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
day=int(input("Enter the day: "))
w_n=weekday_name(year,month,day)
print("The weekday is:",w_n)
