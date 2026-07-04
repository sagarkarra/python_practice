'''
Input:
Check Leap Year

Output:
Enter a year:2026
2026 is not a leap year

Input a year.
Determine whether it is a leap year.

Solution 1:

import calendar as c
year=int(input("Enter the year:"))
if c.isleap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

Solution 2:
'''
import calendar as c
def leap_year(year):
    if c.isleap(year):
        return True
    else:
        return False
year=int(input("Enter the year:"))
c=leap_year(year)
if c:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")