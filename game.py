import random
print("Rock, Paper, Scissors, Shoot!")

# ASK FOR A USER INPUT

playerchoice = input("Please choose either 'rock', 'paper' ,or 'scissors':")

# VALIDATE USER INPUT

if playerchoice == 'rock' or playerchoice == 'paper' or playerchoice =='scissors':
    print("You chose: " + playerchoice)
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()

# GENERATE A COMPUTER CHOICE

computerchoice = ["rock","paper","scissors"]
print("The computer chose: " + random.choice(computerchoice))



# DETERMINE THE WINNER

