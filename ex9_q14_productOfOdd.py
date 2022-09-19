#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#

def product_of_odd(start,end):
    product=1
    for i in range(start, end+1):
        if i%2!=0:
            product=product*i
    return product
ans="y"
while ans=="Y" or ans=="y":
    start=int(input('Enter starting number: '))
    end=int(input('Enter ending number: '))
    print("The product of odd numbers between {0} and {1} is {2} ".format(start,end, product_of_odd(start,end)))
    ans=input('Try again (y/n): ')
