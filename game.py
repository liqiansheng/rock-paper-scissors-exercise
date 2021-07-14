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

choicelist = ["rock","paper","scissors"]
computerchoice = random.choice(choicelist)
print("The computer chose: " + computerchoice)

# DETERMINE THE WINNER

if playerchoice == "rock" and computerchoice == "paper":
    print("You lose!")
elif playerchoice == "paper" and computerchoice == "scissors":
    print("You lose!")
elif playerchoice == "scissors" and computerchoice == "rock":
    print("You lose!")
elif playerchoice == "rock" and computerchoice == "scissors":
    print("You win!")
elif playerchoice == "paper" and computerchoice == "rock":
    print("You win!")
elif playerchoice == "scissors" and computerchoice == "paper":
    print("You win!")
else:
    print("Tie!")

    
    