#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara

def calculate_insurance_primium(oldPremium, numOfAccident):
    if numOfAccident==0:
        increaseRate = 0.02
    elif numOfAccident<3:
        increaseRate=0.05
    elif numOfAccident==3:
        increaseRate=0.1
    elif numOfAccident>3:
        increaseRate=0.3
    newPremium = oldPremium*(1+increaseRate)
    return newPremium
ans="y"
while ans=="Y" or ans=="y":
    oldPremium = float(input('Your current premium: '))
    numOfAccident = int(input('Number of accidents you had: '))
    print("Your new premium is: ", round(calculate_insurance_primium(oldPremium, numOfAccident),2))
    ans=input('Try again (y/n): ')