# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#
import math

number=-1
while number<1:
    number=float(input('Enter radius: '))
    if number<0:
        print('Invalid input. please try again!')
print("area: ", round(number*number*math.pi,2))
print("circumference: ", round(number*2*math.pi,2))
print("diameter: ", round(number*2*math.pi, 2))