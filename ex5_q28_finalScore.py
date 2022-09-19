#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara


def calculate_final_score(num1, num2, num3, num4, num5, num6):
    sum = num1+num2+num3+num4+num5+num6
    finalSum = sum - min(num1, num2, num3, num4, num5, num6)-max(num1, num2, num3, num4, num5, num6)
    finalScore = round(finalSum/4, 2)
    return finalScore
ans="y"
while ans=="Y" or ans=="y":
    score1, score2, score3, score4, score5, score6 = input('Enter 6 scores: ').split(" ")
    print("The final score is: ", calculate_final_score(float(score1), float(score2), float(score3), float(score4), float(score5), float(score6)))
    ans=input('Try again (y/n): ')