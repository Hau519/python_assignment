#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def conver_binary_decimal(number):
    digits = len(str(number))
    decimal=0
    for i in range (digits, 0, -1):
        division = 1
        for j in range (1, i):
            division = division*10
        decimal=decimal+(int((number/division))*(2**(i-1)))
        number = number - int(number/division)*division
    print("decimal is: ", decimal)
ans="y"
while ans=="Y" or ans=="y":
    number=-1
    while number<1:
        number=int(input('Enter a positive binary number: '))
        if number<0:
            print('Invalid input. please try again!')
    conver_binary_decimal(number)
    ans=input('Try again (y/n): ')