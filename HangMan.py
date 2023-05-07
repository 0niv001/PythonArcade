import random

word_list = ["aardvark", "baboon", "camel"]

def hangman():
    on = True
    while on:
        word_show = []
        lives = 6
        secret_word = random.choice(word_list)
        for i in range(len(secret_word)):
            word_show.append("_")
        while lives != 0 and "_" in word_show:
            word_str = ""
            for char in word_show:
                word_str += char
            print(word_str)
            guess = input("Guess a letter: ").lower()
            if guess not in secret_word:
                lives -= 1
                print(f"You guessed {guess}, that's not in the word. You have {lives} lives left.")
            else:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        word_show[i] = guess
            if "_" not in word_show:
                print(f"Well done, the word was {secret_word}, you guessed it")
            if lives == 0:
                print(f"Game Over. The word was {secret_word}")
        again = input("Would you like to play again? Type yes or no\n").lower()
        if again == "no":
            on = False

