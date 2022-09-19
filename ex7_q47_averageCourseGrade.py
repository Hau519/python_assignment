#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
#


def average_grade(weight1, weight2, weight3, weight4):
    grade1=float(input('Enter your 1st assignment grade: '))
    grade2=float(input('Enter your 2nd assignment grade: '))
    grade3=float(input('Enter your mid-exam grade: '))
    grade4=float(input('Enter your final exam grade: '))
    average = (grade1*weight1+grade2*weight2+grade3*weight3+grade4*weight4)/100
    return average

def average_course_grade(numOfStudent):
    total =0
    sum=0
    while total!=100.0:
        weight1=float(input('Enter your 1st assignment weight: '))
        weight2=float(input('Enter your 2nd assignment weight: '))
        weight3=float(input('Enter your mid-exam weight: '))
        weight4=float(input('Enter your final exam weight: '))
        total = weight1+weight2+weight3+weight4
    for i in range (0, numOfStudent):
        print("Student", i+1)
        average = average_grade(weight1, weight2, weight3, weight4)
        sum=sum+ average
    return round(sum/numOfStudent, 2)

ans="y"
while ans=="Y" or ans=="y":
    numOfStudent = int(input('Enter number of student: '))
    print("Average course grade is: ", average_course_grade(numOfStudent))
    ans=input('\nTry again (y/n): ')