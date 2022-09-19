#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara


def is_triangle(side1, side2, side3):
    if side1+side2>side3 or side1+side3>side2 or side3+side2>side1:
        if side1==side2==side3:
            print("This is an equilateral triangle")
        elif side1==side2 or side1==side3 or side2==side3:
            print("This is an isosceles triangle")
        else:
            print("This is a scalene triangle")
    else:
        print("This is not a triangle")
ans="y"
while ans=="Y" or ans=="y":
    side1, side2, side3 = input('Please enter 3 numbers (separate by space) : ').split(" ")
    is_triangle(float(side1), float(side2), float(side3))
    ans=input('Try again (y/n): ')