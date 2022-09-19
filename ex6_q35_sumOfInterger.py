#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara

def sum_between_integers(num1,num2):
    sum=0
    for i in range(min(num1, num2), max(num1, num2)+1):
        sum=sum+i
    return sum
ans="y"
while ans=="Y" or ans=="y":
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    print('Sum between {0} and {1} is {2}'.format(min(num1, num2), max(num1, num2), sum_between_integers(num1, num2)))
    ans=input('Try again (y/n): ')