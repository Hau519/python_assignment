#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def factorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial = factorial*i
    return factorial
ans="y"
while ans=="Y" or ans=="y":
    number=-1
    while number<1:
        number=int(input('Enter a positive number: '))
        if number<0:
            print('Invalid input. please try again!')
    print("The factorial is: ", factorial(number))
    ans=input('Try again (y/n): ')