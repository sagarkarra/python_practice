'''
Input:
Last Working Day

Find the last weekday (Mon–Fri) of a given month
'''
import calendar as c
year=int(input("Enter a year:"))
month=int(input("Enter a month:"))
cal=c.monthcalendar(year,month)
for i in cal:
    if i