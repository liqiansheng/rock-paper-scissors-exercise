import random
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

user_name = os.getenv("USER_NAME")

print("Hi", user_name) # reads the variable from the environment
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

choicelist = ["rock","paper","scissors"]
computerchoice = random.choice(choicelist)
print("The computer chose: " + computerchoice)

# DETERMINE THE WINNER

if playerchoice == "rock" and computerchoice == "paper":
    print("Computer wins!")
elif playerchoice == "paper" and computerchoice == "scissors":
    print("Computer wins!")
elif playerchoice == "scissors" and computerchoice == "rock":
    print("Computer wins!")
elif playerchoice == "rock" and computerchoice == "scissors":
    print("You win!")
elif playerchoice == "paper" and computerchoice == "rock":
    print("You win!")
elif playerchoice == "scissors" and computerchoice == "paper":
    print("You win!")
else:
    print("Tie! Good luck next time!")

print("Thank you for playing!")

    
    