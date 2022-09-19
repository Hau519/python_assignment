#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara

import datetime
from datetime import timedelta
day, month, year = input('enter date 1 DD-MM-YYYY: ').split("-")
date=datetime.date(int(year), int(month), int(day))
nextDate = date+ timedelta(days=1)
print("The next date is: ", nextDate)
