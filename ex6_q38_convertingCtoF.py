#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
# check if it's a prime number

from tabulate import tabulate
ans="y"
while ans=="Y" or ans=="y":
    listC=['C']
    listF=['F']
    start=float(input("Enter starting C degree: "))
    end=float(input("Enter ending C degree: "))
    while start < end+1:
        listC.append(start)
        f = (9*start/5)+32
        listF.append(f)
        start = start + 5
    print(tabulate((listC, listF)))
    ans=input('Try again (y/n): ')





