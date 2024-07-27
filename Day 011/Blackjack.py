# Blackjack Game
import random
from replit import clear
from logo import logo

# Cards and their scores
cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "K": 10, "Q": 10, "A": 11}


def deal_cards():
    """Selects a random card from the cards dictionary."""
    random_card = random.choice(list(cards.items()))
    return random_card


def calculate_score(card_list):
    """Takes a list of cards and return the score calculated from the cards."""
    score = 0
    for card in card_list:
        score += cards[card]

        # Checking for a Blackjack. Blackjack appears when the score is equal to 21 and a hand with only two cards.
        if len(card_list) == 2 and score == 21:
            return 0
        # Checking for an Ace and if the score crosses 21, we change the Ace score to 1.
        # Since Ace is considered 11 initially, we subtract 10 to consider it as 1
        if card == "A" and score > 21:
            score -= 10

    return score


def compare_score(user, computer):
    """Compares the scores of the user and the computer and returns a comment."""
    if user == computer:
        return "Draw 🫡"
    elif computer == 0:
        return "Computer has a Blackjack 🤯. You lose!"
    elif user == 0:
        return "You have a Blackjack 😎. You win!"
    elif  user > 21:
        return "You went over 21 😫. You lose!"
    elif computer > 21:
        return "Computer went over 21 😏. You win!"
    elif user > computer:
        return "You win 😎."
    else:
        return "You lose 😫."


def blackjack():
    clear()
    print(logo)
    # Drawing two random cards for the user
    user_cards = []
    computer_cards = []
    for _ in range(2):
        # Dealing for the user
        user_deal = deal_cards()
        user_cards.append(user_deal[0])

        # Dealing for the computer
        computer_deal = deal_cards()
        computer_cards.append(computer_deal[0])

    # Flag
    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        # If the game is not over, we ask the user if they want to deal more cards.
        else:
            deal_more = input("Do you want to \"Hit\" (Type H) or \"Stand\" (Type S)? ").lower()
            if deal_more == "h":
                user_cards.append(deal_cards()[0])
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards()[0])
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}.")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}.")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of BlackJack and deal? Type 'y' or 'n': ").lower() == 'y':
    blackjack()
