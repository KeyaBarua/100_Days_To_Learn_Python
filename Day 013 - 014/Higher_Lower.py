from game_data import accounts
import art
import random
from replit import clear


def get_random_data():
    """Gets a random number between 1 and 100."""
    data = random.choice(accounts)
    return data


def get_account_with_high_followers(account1, account2):
    """Gets the numbers from the followers value, converts into int and then returns the highest number."""
    f1 = float(account1["followers"][:-1])
    f2 = float(account2["followers"][:-1])
    if f1 > f2:
        return 'A'
    else:
        return 'B'


# Get the second random account
account_b = get_random_data()

# Flags
score = 0
answer_wrong = False

while not answer_wrong:
    # Printing the logo
    print(art.logo)
    
    # Put the second random account in the first
    account_a = account_b
    account_b = get_random_data()
    # Getting new random data until both accounts are not same
    while account_a == account_b:
        account_b = get_random_data()

    # Printing the data
    print(f"Compare A: {account_a['name']}, a(n) {account_a['description']} from "
          f"{account_a['country']}.")
    print(art.versus)
    print(f"Against B: {account_b['name']}, a(n) {account_b['description']} from "
        f"{account_b['country']}.")

    # Getting the account with the highest followers
    highest_follower_account = get_account_with_high_followers(account_a, account_b)

    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    clear()
    
    # Checking the user guess and the highest follower account
    if user_answer == highest_follower_account:
        score += 1
        print(f"You're right. Your current score is {score}.\n")
    else:
        print(f"Sorry! You're wrong. Your final score is {score}.")
        answer_wrong = True

