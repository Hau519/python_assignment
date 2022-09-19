#
# @Name: Hau Vu
# @Date: Sept 19, 2022
# Assignment 2 - Dara
# Dispaying different sequences

#sequence: 5 10 15 20 25 30 35 40
def displaying_sequence_5(start, numOfNumbers):
    count=0
    while count<numOfNumbers:
        print(start, end=" ")
        start = start + 5
        count+=1
#sequence: 3 5 7 9 11 13 15
def displaying_sequence_2(start, numOfNumbers):
    count=0
    while count<numOfNumbers:
        print(start, end=" ")
        start = start + 2
        count+=1
#sequence 80 70 ...20
def displaying_sequence_negative10(start, numOfNumbers):
    count=0
    while count<numOfNumbers:
        print(start, end=" ")
        start = start - 10
        count+=1
#sequence 1 2 6 24 120 720
def displaying_sequence_multiple(start, numOfNumbers):
    count=1
    while count<numOfNumbers+1:
        print(start, end=" ")
        start = start*(count+1)
        count+=1
print("\nSequence +5: ")
displaying_sequence_5(5, 8)
print("\nSequence +2: ")
displaying_sequence_2(3, 7)
print("\nSequence -10: ")
displaying_sequence_negative10(80, 7)
print("\nSequence *n: ")
displaying_sequence_multiple(1, 6)
print("\n")
ans=input('Do you want any sequence? (Y/N)')
while ans=="Y" or ans=="y":
    choice=int(input("Enter your choice: \n1. Sequence +5\n2. Sequence +2\n3. Sequence -10\n4.Sequence *n\n"))
    start=int(input('Enter starting number: '))
    numOfNumbers=int(input('Enter number of numbers in the sequence: '))
    match choice:
        case 1:
            displaying_sequence_5(start, numOfNumbers)
        case 2:
            displaying_sequence_2(start, numOfNumbers)
        case 3:
            displaying_sequence_negative10(start, numOfNumbers)
        case 4:
            displaying_sequence_multiple(start, numOfNumbers)
        case _:
            print("Your choice is not valid")
    ans=input('Try again (y/n): ')