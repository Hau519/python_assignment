#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
# min max of 1000 numbers

from __future__ import division
def min_max_list_number(numOfNumber):
    list = []
    count=0
    while count<numOfNumber:
        num = int(input("Enter number: "))
        list.append(num)
        count+=1
    print("Min of all number is: ", min(list))
    print("Min of all number is: ", max(list))
ans="y"
while ans=="Y" or ans=="y":
    numOfNumber = int(input('Enter number of numbers: '))
    min_max_list_number(numOfNumber)
    ans=input('Try again (y/n): ')
