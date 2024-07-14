# HANGMAN Game
import random

from replit import clear

import word_list as wl
from hangman_lives import HANGMANPICS as lives
from hangman_logo import logo

print(logo)

# Generating a random word and blanks
choice = random.choice(wl.word_list)
random_word = choice[0]
print(f"Hint: {choice[1]}")
display = []
lives_lost = 0
for _ in random_word:
    display.append("_")


# Looping until there are no blanks in the list
end_of_game = False
while not end_of_game:
    # Asking the user to guess a letter
    guess_letter = input("Guess a letter:\n").lower()
    clear()

    for position in range(len(random_word)):
        letter = random_word[position]
        # If the user guesses a correct letter
        if letter == guess_letter:

            # If the user guesses same letter multiple times.
            if guess_letter in display:
                print(f"You've already guessed {guess_letter}.")

            display[position] = letter

            # If there are no more blanks, the game is over.
            if "_" not in display:
                end_of_game = True
                print(f"You're right! The word is ")

    # Printing the characters in the list as a string
    print(' '.join(display))

    # If the user guesses a wrong letter
    if guess_letter not in random_word:
        print(f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        print(lives[lives_lost])
        lives_lost += 1

        # If the number of lives lost is equal to the length of the list of lives, the game is over.
        if lives_lost == len(lives):
            print(f"You lost! The word is {random_word}.")
            end_of_game = True
