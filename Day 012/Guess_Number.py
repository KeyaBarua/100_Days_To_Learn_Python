from art import logo
import random
print(logo)

# Constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def compare_guess(hidden_num, user_guess):
    """Compares the user guess and the secret number and returns a message."""
    if user_guess == hidden_num:
        return 0
    elif user_guess > hidden_num:
        return 1
    else:
        return -1


def attempts_remaining(level):
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def game():
    # Welcome message
    print("Welcome to the Number Guessing game!")
    print("I am thinking of a number between 1 and 100.")
    # Computer choosing a random number from 1 to 100
    secret_number = random.randint(1, 100)

    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    # Getting the number of attempts based on the difficulty level
    attempts = attempts_remaining(difficulty)

    # Flag
    to_continue = True
    while to_continue:
        # If number of attempts become 0, we end the function.
        if attempts == 0:
            print("You've run out of attempts. You lose!")
            print(f"The number was {secret_number}.")
            return

        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        result = compare_guess(secret_number, guess)

        # Conditions
        if result == 1:
            print("Too High.\nGuess again.\n")
            attempts -= 1
        elif result == -1:
            print("Too Low.\nGuess again.\n")
            attempts -= 1
        else:
            print(f"You got it! The number was {secret_number}.")
            to_continue = False


game()
