import random

# Mapping of user input to game values
youDict = {"r": 0, "p": 1, "s": 2}
reverseDict = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Random computer choice
computer = random.choice([0, 1, 2])

# User input
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()

# Input validation
if youstr not in youDict:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
else:
    you = youDict[youstr]

    # Display choices
    print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

    # Game logic
    if you == computer:
        print("It's a draw!")
    elif (you == 0 and computer == 2) or (you == 1 and computer == 0) or (you == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
