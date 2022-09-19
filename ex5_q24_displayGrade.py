#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara


def display_grade(grade):
    if grade<60:
        gradeLetter = "F"
    elif grade <70:
        gradeLetter = "D"
    elif grade < 80:
        gradeLetter = "C"
    elif grade < 90:
        gradeLetter = "B"
    else:
        gradeLetter ="A"
    return gradeLetter
ans="y"
while ans=="Y" or ans=="y":
    grade = float(input("Please enter your grade: "))
    print("Your letter grade is: ", display_grade(grade))
    ans=input('Try again (y/n): ')