#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def display_prime(startNumber, endNumber):
    for i in range (startNumber, endNumber+1):
        count=0
        for j in range (2, i):
            if i%j==0:
                count+=1
        if count==0:
            print(i, end=" ")
ans="y"
while ans=="Y" or ans=="y":
    startNumber = int(input('Enter starting number: '))
    endNumber= int(input('Enter ending number: '))
    display_prime(startNumber, endNumber)
    ans=input('\nTry again (y/n): ')
