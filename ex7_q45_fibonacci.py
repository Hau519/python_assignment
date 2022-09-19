#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def fibonacci(numOfNumbers):
    num1=1
    num2=1
    for i in range (2, numOfNumbers):
        print(num1, end=" ")
        print(num2, end=" ")
        num1=num1+num2
        num2=num1+num2
ans="y"
while ans=="Y" or ans=="y":
    numOfNumbers=int(input('Enter number of numbers in Fibonacci you want to display: '))
    fibonacci(numOfNumbers)
    ans=input('\nTry again (y/n): ')