import random

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
on = True


# Functions
def add_card(who):
    who.append(random.choice(cards))


def score_count(hand, score):
    score *= 0
    for card in hand:
        score += card
    return score


def score_print():
    return print(f"Your cards: {p_hand}, current score: {p_score} \nComputer's first card: {c_hand[0]}")


def showdown():
    print(f"Your final hand: {p_hand}, final score: {p_score}")
    print(f"Computer's final hand: {c_hand}, final score: {c_score}")
    if (c_score > 21) or (p_score < 21) and (p_score > c_score):
        print("You win")
    else:
        print("You lose")


# Play
while on:
    p_hand = []
    c_hand = []
    p_score = 0
    c_score = 0
    hit = "a"
    if input("Do you want to play a game of BlackJack? Type 'y' or 'n'\n") == "n":
        on = False
    else:
        # Deal cards
        for i in range(2):
            add_card(p_hand)
            add_card(c_hand)
        # Add up scores
        p_score = score_count(p_hand, p_score)
        c_score = score_count(c_hand, c_score)
        # Play round
        score_print()
        while hit != "n" and p_score <= 21:
            hit = input("Type 'y' to get another card, type 'n' to pass \n").lower()
            if hit == "y":
                add_card(p_hand)
                p_score = score_count(p_hand, p_score)
                score_print()
            else:
                if c_score <= 17:
                    add_card(c_hand)
                    c_score = score_count(c_hand, c_score)
        showdown()
