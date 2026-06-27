'''
Input:
Print All Mondays

Output:
Enter year:2026
Enter month:6
Monday dates are:
June 1
June 8
June 15
June 22
June 29
Given a month and year, print all dates that fall on Monday

Solution 1:
import calendar as c
year = int(input("Enter year:"))
month = int(input("Enter month:"))
print("Monday dates are:")
cal = c.monthcalendar(year, month)
m_n=c.month_name[month]
for week in cal:
    monday = week[0]
    if monday != 0:
        print(f"{m_n} {monday}")

Solution 2:
'''
import calendar as c
def only_mondays(year, month):
    cal = c.monthcalendar(year, month)
    print("Mondays are:")
    for week in cal:
        if week[0] != 0:
            print(week[0])

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(f"Month: {c.month_name[month]}")
only_mondays(year, month)