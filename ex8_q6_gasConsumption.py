#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

ans="y"
while ans=="Y" or ans=="y":
    litre = float(input('Enter number of litres used: '))
    km = float(input('Enter number of km travaled: '))
    print("Rate of gas consumption per 100km is: ", round(litre/km,2)*100)
    ans=input('Try again (y/n): ')
