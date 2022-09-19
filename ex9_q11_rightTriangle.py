#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
import math


def is_ringt_angled_triangle(side1, side2, side3):
    if math.sqrt(side1**2+side2**2)==side3 or math.sqrt(side1*2+side3**2)==side2 or math.sqrt(side3**2+side2**2)==side1:
        print("This is a right-angled triangle")
    else:
        print("This is not a right-angled triangle")
ans="y"
while ans=="Y" or ans=="y":
    side1, side2, side3 = input('Please enter 3 numbers (separate by space) : ').split(" ")
    is_ringt_angled_triangle(float(side1), float(side2), float(side3))
    ans=input('Try again (y/n): ')