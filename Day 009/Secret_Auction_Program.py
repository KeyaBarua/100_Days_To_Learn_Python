# Secret Auction Program
import art
from replit import clear

print(art.logo)
print("Welcome to the Secret Auction Program")

play_bidding = True
# Empty dictionary
bidder_dict = {}


def get_highest_bidder(bidders):
    max_amount = 0
    for bidder in bidders:
        if bidders[bidder] > max_amount:
            highest_bidder = bidder
            max_amount = bidders[bidder]

    print(f"The winner is {highest_bidder} with a bid of ${max_amount}.")


while play_bidding:
    bidder_name = input("What's your name?: ").title()
    bidding_amount = int(input("What's your bid?: "))
    # Storing the name and amount in the dictionary
    bidder_dict[bidder_name] = bidding_amount

    # Asking if there are any other bidders
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    clear()

    # print(bidder_dict)
    if other_bidder == "no":
        # Calling the function to display the highest bidder.
        get_highest_bidder(bidder_dict)
        play_bidding = False
