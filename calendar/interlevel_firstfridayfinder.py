'''
Input:
First Friday Finder
Output:
Enter a year:2026
Enter a month:6
TheFirst friday of June 2026 is: 5
Find the first Friday of a given month and year

import calendar as c
year=int(input("Enter a year:"))
month=int(input("Enter a month:"))
cal=c.monthcalendar(year,month)
m_n=c.month_name[month]
for i in cal:
    if i[4]!=0:
        print(f"The First friday of {m_n} {year} is:",i[4])
        break;


Solution 2:
'''
import calendar as c
def first_friday(year, month):
    cal = c.monthcalendar(year, month)
    for i in cal:
        if i[4] != 0:   # Friday is at index 4
            return i[4]
year = int(input("Enter year: "))
month = int(input("Enter month: "))
month_name = c.month_name[month]
friday_find = first_friday(year, month)
print(f"The first Friday of {month_name} {year} is {friday_find}.")
