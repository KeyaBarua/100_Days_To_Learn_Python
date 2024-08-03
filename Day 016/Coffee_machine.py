from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

# Objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


coffee_machine_on = True
while coffee_machine_on:
    user_choice = input(f"What would you like ({menu.get_items()})?: ").lower()
    if user_choice == "off":
        coffee_machine_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Checking if the resources are sufficient
        if coffee_maker.is_resource_sufficient(menu.find_drink(user_choice)):
            # Checking if the transaction is successful
            if money_machine.make_payment(menu.find_drink(user_choice).cost):
                coffee_maker.make_coffee(menu.find_drink(user_choice))
