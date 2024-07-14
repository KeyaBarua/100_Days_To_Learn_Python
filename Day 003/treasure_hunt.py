# ASCII art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if direction == "left":
    # continue in the game
    to_do = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a "
                  "boat. Type \"swim\" to swim across.\n").lower()
    if to_do == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one "
                      "blue. Which color do you choose?\n").lower()
        if color == "blue":
            print("You enter a room full of beasts. Game over!")
        elif color == "red":
            print("There is fire in the room. Game over!")
        else:
            print("You found the treasure. YOU WIN!")
    else:
        print("There is a float of crocodiles nearby. Game over!")
else:
    print("Oh no! You fell into a hole. Game over.")
