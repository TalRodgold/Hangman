import calendar
import datetime
from datetime import date
import calendar
def findDay(date):
    day, month, year = (int(i) for i in date.split(' '))
    born = datetime.date(year, month, day)
    return born.strftime("%A")
day = input("pleas enter date here\n")
print(findDay(day))
