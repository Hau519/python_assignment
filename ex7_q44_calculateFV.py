#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def calculate_fv(amount, numOfYear, interestPerYear):
    pv = amount*((1+interestPerYear/100)**numOfYear)
    return round(pv,2)
ans="y"
while ans=="Y" or ans=="y":
    amount=float(input('Enter your amount you want to invest: '))
    numOfYear=int(input('Number of years you want to invest: '))
    interestPerYear=int(input('Enter interest per year (%): '))
    print("Your investment will worth: ", calculate_fv(amount, numOfYear, interestPerYear))
    ans=input('Try again (y/n): ')