from logo import logo
from replit import clear

print(logo)


def add_numbers(number1, number2):
    """Returns the sum of 2 numbers."""
    return number1 + number2


def sub_numbers(number1, number2):
    """Returns the difference of 2 numbers."""
    return number1 - number2


def mul_numbers(number1, number2):
    """Returns the product of 2 numbers."""
    return number1 * number2


def  div_numbers(number1, number2):
    """Returns the quotient of 2 numbers."""
    return number1 / number2


def calculator():
    """Produces the result of two numbers after performing the operation specified."""
    operations = {"+": add_numbers,
                           "-" : sub_numbers,
                           "*": mul_numbers,
                           "/": div_numbers,
                         }

    first_number = float(input("What's the first number?: "))

    # Displaying the operation symbols
    for key in operations:
        print(key)

    oper_symbol = input("Pick an operation: ")
    # Getting the value from the operations dictionary
    operation_to_do = operations[oper_symbol]

    next_number = float(input("What's the next number?: "))
    result = operation_to_do(first_number, next_number)

    print(f"{first_number} {oper_symbol} {next_number} = {result}")

    to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, "
                            f"or type 'AC' to exit: "
                            f"").lower()
    if to_continue == "y":
        # Making the first number equal to result to continue calculating with the previous result
        first_number = result
    elif to_continue == "n":
        clear()
        calculator()


calculator()
