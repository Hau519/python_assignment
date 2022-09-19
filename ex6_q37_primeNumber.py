#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
# check if it's a prime number

def is_prime(number):
    for i in range(2, number):
        if number%i==0:
            print(number, "is not prime number")
            return
    print(number, "is a prime number")
ans="y"
while ans=="Y" or ans=="y":
    number=-1
    prime=0
    while number<1:
        number=int(input('Enter a positive number: '))
        if number<0:
            print('Invalid input. please try again!')
    is_prime(number)
    ans=input('Try again (y/n): ')
