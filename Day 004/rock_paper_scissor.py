# A game of rock, paper and scissor with computer.
import game_art
import random

# User choice
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissor.\n"))

# Checking if the user entered an invalid number
if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number.")

else:
    print(game_art.option[user_choice])

    # Computer Choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_art.option[computer_choice]}")

    # Determining the winner
    # Draw case
    if user_choice == computer_choice:
        print("It's a draw!")

    # Computer wins
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2
        and computer_choice == 0):
        print("You lose!")

    # User wins
    else:
        print("You win!")
