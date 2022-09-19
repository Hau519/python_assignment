#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def encrypting(number):
    if number<1000 or number>9999:
        print("Please enter positive 4-digit number. ")
        return
    else:
        num1=int(number/1000)
        num2=int((number-num1*1000)/100)
        num3=int((number-num1*1000-num2*100)/10)
        num4=int((number-num1*1000-num2*100-num3*10))
    enNum1=(num1+7)%10
    enNum2=(num2+7)%10
    enNum3=(num3+7)%10
    enNum4=(num4+7)%10
    enNumber = enNum3*1000+enNum4*100+enNum1*10+enNum2
    return enNumber
def decrypt_digit(digit):
    if digit>=7:
        decrypt_digit = digit-7
    else:
        decrypt_digit = digit+10-7
    return decrypt_digit
def decrypting(enNumber):
    enNum1=int(enNumber/1000)
    enNum2=int((enNumber-enNum1*1000)/100)
    enNum3=int((enNumber-enNum1*1000-enNum2*100)/10)
    enNum4=int((enNumber-enNum1*1000-enNum2*100-enNum3*10))
    num1 = decrypt_digit(enNum1)
    num2 = decrypt_digit(enNum2)
    num3 = decrypt_digit(enNum3)
    num4 = decrypt_digit(enNum4)
    number = num3*1000+num4*100+num1*10+num2
    return number
ans="y"
while ans=="Y" or ans=="y":
    number=int(input("Enter a positive 4-digit number: "))
    encrypt = encrypting(number)
    print("encrypted number is: ", encrypt )
    print("decrypted number is: ",decrypting(encrypt))
    ans=input('Try again (y/n): ')