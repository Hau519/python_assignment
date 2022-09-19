#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
# average of 1000 grades

def average_list_number(numOfGrades):
    list = []
    count=0
    sum=0
    while count<numOfGrades:
        num = int(input("Enter grade"),count+1, ": ")
        sum = sum+num
        count+=1
    return round(sum/numOfGrades,2)

ans="y"
while ans=="Y" or ans=="y":
    numOfGrades = int(input('Enter number of grades: '))
    print("Average of grades is: ",average_list_number(numOfGrades))
    ans=input('Try again (y/n): ')
