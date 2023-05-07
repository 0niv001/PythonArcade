import random


def rps_round():
    p_score, c_score, game = 0, 0, True
    choices = ["Rock", "Paper", "Scissors"]
    while game:
        user_choice = -1
        computer_choice = random.randint(0, 2)
        while user_choice not in range(0, 3):
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
        print(f"You picked {choices[user_choice]}. The computer picked {choices[computer_choice]}")
        if user_choice == computer_choice:
            print("It's a draw")
        elif not (not (user_choice == 0 and 1 == computer_choice) and not (
                user_choice == 1 and 2 == computer_choice) and not (user_choice == 2 and computer_choice == 0)):
            c_score += 1
            print("You Lose")
        else:
            p_score += 1
            print("You Win")
        print(f"The score is: You {p_score} | Computer {c_score}")
        if input("Play again? Type yes or no \n").lower() == "no":
            game = False