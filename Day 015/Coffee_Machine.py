# Making a Coffee Machine
# Espresso - 50ml water, 18g coffee, $1.50
# Latte - 200ml water, 24g coffee, 150ml milk, $2.50
# Cappuccino - 250ml water, 24g coffee, 100ml milk, $3.00
# Resources - 500ml water, 300ml milk, 200g coffee
# Coins - Penny($0.01), Nickel(0.05), Dime($0.10), Quarter($0.25)
# Requirements:
# Print report, Check resources sufficient, process coins, check transaction successful, make coffee if transaction is successful

MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.25
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.50
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.00
    },
}

resources = {
    "water": 500,
    "coffee": 200,
    "milk": 300
}

money = 0


# Printing report
def make_report():
    """Prints the resources available in the coffee machine"""
    print(f"Water: {resources['water']}\nCoffee: {resources['coffee']}\nMilk: {resources['milk']}\nMoney: ${money}")


def check_resources_sufficient(drink):
    """Checks if the resources amount are greater than the amount required in making the drink."""
    for item in MENU[drink]['ingredients']:
        if resources[item] < MENU[drink]['ingredients'][item]:
            print(f"Sorry, there is not enough {item}")
            return False
        return True


def calculate_total(qrts, dim, nick, pen):
    """Calculates the total money by adding the number of quarters, dimes, nickels and pennies"""
    total = (qrts * 0.25) + (dim * 0.10) + (nick * 0.05) + (pen * 0.01)
    return total


def make_a_drink(drink):
    """Subtracts the required amount of ingredients for the drink from the resources"""
    for item in MENU[drink]['ingredients']:
        resources[item] -= MENU[drink]['ingredients'][item]


def want_a_drink():
    """Starts the coffee machine"""
    coffee_machine_on = True
    while coffee_machine_on:
        user_choice = input("What would you like? (espresso / latte / cappuccino): ").title()
        global money

        if user_choice == "Report":
            make_report()
        elif user_choice == "Off":
            coffee_machine_on = False
        else:
            if check_resources_sufficient(user_choice):
                print("Please insert coins.")
                # Process the coins
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))
                total_money = calculate_total(quarters, dimes, nickels, pennies)
                if total_money >= MENU[user_choice]['cost']:
                    make_a_drink(user_choice)
                    money += MENU[user_choice]['cost']
                    change = total_money - MENU[user_choice]['cost']
                    print(f"Here is ${round(change, 2)} in change.\nHere is your"
                          f" {user_choice}☕. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")


want_a_drink()

