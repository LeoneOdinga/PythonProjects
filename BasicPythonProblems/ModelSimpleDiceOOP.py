from random import randint

class Die():

     # function to instantiate each die object with the number of sides it has

    def __init__(self,numberOfSides):
        self.numberOfSides = numberOfSides

    def __int__(self):
        self.numberOfSides = 6

     # function to generate a random number between 1 and number of sides the die has when rolled

    def rollDie(self,numberOfTimes):

        for index, i in enumerate(range(numberOfTimes)):
            print(f"\nIn Roll Number {i+1}, You Rolled The Dice To Side {randint(1,self.numberOfSides)} ")

'''The below code should be separated from this class and placed in main program to focus on high level logic, though this is basic we would not require it'''

# let us try to make the program a bit interactive, allow a user to create a die of x sides and roll n times

print("Welcome To The Dice Rolling Program! Choose The Number Of Die You Want And How Many Times You Need To Roll it")

userNumberOfSides = int(input("\nEnter The Number Of Sides Of The Die You Need: "))

userDie = Die(userNumberOfSides)

userRollNumber = int(input("How Many Times Do You Want To Roll The Die? "))

userDie.rollDie(userRollNumber)
