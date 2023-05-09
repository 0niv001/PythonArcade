import random

# Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Functions
def add_card(who):
    who.append(random.choice(cards))


def score_count(hand):
    score = sum(hand)
    return score


def check_ace(hand, score):
    for card in hand:
        if card == 11 and score > 21:
            hand[hand.index(11)] = 1
    points = sum(hand)
    return points


def b_21(hand, score):
    if (score == 21) and ((10 in hand) and (11 in hand)):
        return True


def black_jack():
    def showdown():
        print(f"Your final hand: {p_hand}, final score: {p_score}")
        print(f"Computer's final hand: {c_hand}, final score: {c_score}")
        if ((c_score > 21) and (p_score <= 21)) or ((p_score <= 21) and (p_score > c_score)):
            print("You win")
        else:
            print("You lose")

    def score_print():
        return print(f"Your cards: {p_hand}, current score: {p_score} \nComputer's first card: {c_hand[0]}")

    on = True
    while on:
        p_hand = []
        c_hand = []
        p_score = 0
        c_score = 0
        hit = "a"
        if input("Do you want to play a game of BlackJack? Type 'y' or 'n'\n") == "n":
            on = False
        else:
            for i in range(2):
                add_card(p_hand)
                add_card(c_hand)
            check_ace(p_hand, score_count(p_hand))
            p_score = score_count(p_hand)
            score_print()
            if b_21(p_hand,p_score):
                print("BlackJack, You Win")
            else:
                while hit != "n" and p_score <= 21:
                    hit = input("Type 'y' to get another card, type 'n' to pass \n").lower()
                    if hit == "y":
                        add_card(p_hand)
                        check_ace(p_hand, score_count(p_hand))
                        p_score = score_count(p_hand)
                        score_print()
                    if c_score <= 17:
                        add_card(c_hand)
                        check_ace(p_hand, score_count(c_hand))
                        c_score = score_count(c_hand)
                showdown()