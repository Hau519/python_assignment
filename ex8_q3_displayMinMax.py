# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

number1=float(input("Enter first number: "))
number2=float(input("Enter second number: "))
if number2==number1:
    print("Equal number")
else:
    print(max(number2, number1), "is greater than ", min(number2, number1))
