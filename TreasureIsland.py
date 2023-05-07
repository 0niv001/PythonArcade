global game


def again():
    global game
    game = False
    play = input("Do you want to play again? Type yes, or no\n").lower()
    if play == "yes":
        treasure()


def treasure():
    global game
    game = True
    while game:
        print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
        direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
        if direction == "left":
            print("You fall into a trap and you die. Game Over")
            again()
        elif direction == "right":
            swim = input(
                "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. "
                "Type 'swim' to swim across \n").lower()
            if swim == "wait":
                print("You Die")
                again()
            elif swim == "swim":
                colour = input(
                    "You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one "
                    "blue. Which colour do you choose? \n").lower()
                if colour == "red":
                    print("It's a room full of fire. Game over")
                    again()
                elif colour == "blue":
                    print("A shark attacks you. Game over")
                    again()
                elif colour == "yellow":
                    print("You found the treasure")
                    again()
                else:
                    print("Not a valid colour. Game Over")
                    again()
            else:
                print("Not a valid action. You die")
                again()
        else:
            print("Not a valid direction. You die")
            again()
