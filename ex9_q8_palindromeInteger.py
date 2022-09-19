#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def is_palindrome(number):
    if number<10000 or number>99999:
        print("Please enter positive 5-digit number. ")
        return
    else:
        num1=int(number/10000)
        num2=int((number-num1*10000)/1000)
        num3=int((number-num1*10000-num2*1000)/100)
        num4=int((number-num1*10000-num2*1000-num3*100)/10)
        num5=int(number-num1*10000-num2*1000-num3*100-num4*10)
    if num1==num5 and num2==num4:
        print(number, "is a palindrome number")
    else:
        print(number, "is not a palindrome number")
ans="y"
while ans=="Y" or ans=="y":
    number=int(input("Enter a positive 5-digit number: "))
    is_palindrome(number)
    ans=input('Try again (y/n): ')