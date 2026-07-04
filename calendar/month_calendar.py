'''
Input:
Display a Month Calendar
Take a year and month as input.
Print the calendar for that month using the calendar module.

Output:
Enter the year:2026
Enter month:6
Month calendar of June is:
      June 2026
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30

Solution 1:
import calendar as c
year=int(input("Enter the year:"))
month=int(input("Enter month:"))
print("Month calendar is:",c.monthcalendar(year,month))

Solution 2:
'''
import calendar as c
def month_calendar(year,month):
    m_c=c.month(year,month)
    return m_c
year=int(input("Enter the year:"))
month=int(input("Enter month:"))
month_name = c.month_name[month]
m_c=month_calendar(year,month)
print(f"Month calendar of {month_name} is:\n",m_c)
