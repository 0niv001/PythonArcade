import random


def difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    if choice == 'hard':
        return 5
    elif choice == "easy":
        return 10


def num_guess():
    on = True
    print("Welcome to the Number Guessing Game! \nI'm Thinking of a number between 1 and 100.")
    while on:
        ran_num = random.randrange(0, 101)
        attempts = difficulty()
        # Game
        while attempts >= 0:
            print(f"You have {attempts} attempts to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > ran_num:
                attempts -= 1
                print("Too High")
            elif guess < ran_num:
                attempts -= 1
                print("Too Low")
            if guess == ran_num:
                print(f"You guessed right! {ran_num} was the number.")
                break
            if attempts == 0:
                print("You've run out of guesses, you lose.")
                break
        if input("Do you want to play again? Type 'y' or 'n'").lower() == "n":
            on = False