#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#
from tabulate import tabulate

def calculate_square_cube(start, end):
    numberList=['number']
    squareList=['Square']
    cubeList=['Cube']
    for i in range(start, end):
        numberList.append(i)
        squareList.append(i*i)
        cubeList.append(i*i*i)
    print(tabulate((numberList, squareList, cubeList)))
ans="y"
while ans=="Y" or ans=="y":
    start=int(input("Enter starting number: "))
    end=int(input("Enter ending number: "))
    calculate_square_cube(start, end)
    ans=input('Try again (y/n): ')