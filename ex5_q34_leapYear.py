#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara

def is_leap_year(year):
    if year%400==0:
        print(year,"is a leap year")
    elif year%100==0:
        print(year, "is not a leap year")
    elif year%4==0:
        print(year,"is a leap year")
    else:
        print(year, "is not a leap year")
ans="y"
while ans=="Y" or ans=="y":
    year=int(input("Enter a year: "))
    is_leap_year(year)
    ans=input('Try again (y/n): ')
