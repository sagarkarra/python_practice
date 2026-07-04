'''
Input:
Weekend Counter
Output:
Enter year: 2026
Enter month: 6
Number of Saturdays: 4
Number of Sundays: 4

Count the number of Saturdays and Sundays in a given month

import calendar as c
year=int(input("Enter a year:"))
month=int(input("Enter the month:"))
scount=0
sucount=0
cal=c.monthcalendar(year,month)
for i in cal:
    if i[5]!=0:
        scount+=1
    if i[6]!=0:
        sucount+=1
print("Number of Saturdays:",scount)
print("Number of sundays:",sucount)

Solution 2:
'''
import calendar as c
def weekend_counter(year, month):
    cal = c.monthcalendar(year, month)
    scount = 0
    sucount = 0
    for i in cal:
        if i[5] != 0:
            scount += 1
        if i[6] != 0:
            sucount += 1
    return scount, sucount
year = int(input("Enter year: "))
month = int(input("Enter month: "))
sat, sun = weekend_counter(year, month)
print("Number of Saturdays:", sat)
print("Number of Sundays:", sun)
