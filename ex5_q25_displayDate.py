#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara


import datetime
day1, month1, year1 = input('enter date 1 DD-MM-YYYY: ').split("-")
day2, month2, year2 = input('enter date 2 DD-MM-YYYY: ').split("-")

date1=datetime.date(int(year1), int(month1), int(day1))
date2=datetime.date(int(year2), int(month2), int(day2))

if date1>date2:
    print(date2, "comes before", date1)
else:
    print(date1, "comes before", date2)

