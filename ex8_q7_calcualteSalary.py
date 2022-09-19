#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

ans="y"
while ans=="Y" or ans=="y":
    sales = float(input('Enter the representative’s sales in dollars '))
    print("The representative’s salary is : ", round(200+sales*0.09))
    ans=input('Try again (y/n): ')