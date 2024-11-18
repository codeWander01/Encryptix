# ROCK PAPER SCISSORS GAME

import random

# Computer choice is randomly selected from rock, paper, or scissors
computer = random.choice([1, 0, -1])  # 1 for rock, 0 for paper, -1 for scissors

# Get user input
youstr = input("Enter your choice (rock, paper, scissors): ")

# Map user input to corresponding values
youDict = {"rock": 1, "paper": 0, "scissors": -1}
you = youDict[youstr]

# Reverse mapping for displaying choices
revDict = {1: "rock", 0: "paper", -1: "scissors"}

# Display choices
print(f"Your choice: {revDict[you]}\nComputer choice: {revDict[computer]}")

# Game logic
if computer == you:
    print("Game is a draw")
else:
    if you == 1 and computer == -1:  # rock beats scissors
        print("You win!")
    elif you == 0 and computer == 1:  # paper beats rock
        print("You win!")
    elif you == -1 and computer == 0:  # scissors beats paper
        print("You win!")
    else:
        print("Computer wins!")
