# Generate a password.
import random
print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_numbers = int(input("How many numbers would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like in your password?\n"))

# Lists
letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol_list = ['%', '#', '@', '!', '$', '&', '*', '(', ')', '+']

characters = []

# Creating a random character list
for number in range(1, num_of_letters + 1):
    letter = random.choice(letter_list)
    characters.append(letter)

for number in range(1, num_of_numbers + 1):
    num_char = random.choice(number_list)
    characters.append(num_char)

for number in range(1, num_of_symbols + 1):
    sym = random.choice(symbol_list)
    characters.append(sym)

total_char = num_of_letters + num_of_numbers + num_of_symbols
# Empty string
password = ""

# Getting the characters in random
for char in range(0, total_char):
    # Getting a random character from the characters list
    pass_char = random.choice(characters)
    # Concatenating the random character to the password variable
    password += pass_char
    # Removing the character from the list so that it is not concatenated again to the password variable.
    characters.remove(pass_char)

print(password)
