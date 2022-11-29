
import random
import os
import art
from art import logo

deck = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", 
"7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", 
"Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]

def deck_shuffle(main_deck):
    random.shuffle(main_deck)
    return main_deck

def deal(main_deck, cc):
    deal = []
    while cc >= 48:
        deal.append(main_deck[0 + cc])
        cc -= 1
    return deal

def start_score(hand):
    score = 0
    for c in hand:
        if c == 'A':
            score += 11
        elif c == 'J' or c == 'Q' or c == 'K':
            score += 10
        else: 
            score += int(c)
    return score

while True:
    deck_shuffle(deck)
    deal_track = 51
    starting_deal = deal(deck, deal_track)

    play_hand = [deal(deck, deal_track)[0], deal(deck, deal_track)[1]]
    comp_hand = [deal(deck, deal_track)[2], deal(deck, deal_track)[3]]
    play_score = start_score(play_hand)
    comp_score = start_score(comp_hand)

    print(art.logo)
    print(f"Your cards: {play_hand}, current score: {play_score}")
    print(f"Computers first card: {comp_hand[0]}")

    deck_cycle = 0
    current_card = deck[48 - deck_cycle]
    p_score = play_score
    c_score = comp_score
    card_value = 0
    choice = "y"
    choice = input("Type 'y' to HIT and get another card, and type 'n' to PASS: ")

    while choice == "y":
        deck_cycle += 1
        if current_card == 'A':
            ace_choice = int(input("Do you want the ace to be a 1 or 11? Type '1' or '11' to choose: "))
            if ace_choice == 1:
                card_value = 1
            else: card_value = 11
        elif current_card == 'J' or current_card == 'Q' or current_card == 'K':
            card_value = 10
        else: card_value = int(current_card)

        if (p_score + card_value) > 21:
            p_score += card_value
            play_hand.append(current_card)
            break
        else:
            p_score += card_value
            play_hand.append(current_card)
            print(f"Your cards: {play_hand}, current score: {p_score}")
            print(f"Computer's first card: {comp_hand[0]} ")
            choice = input("Type 'y' to HIT and get another card, and type 'n' to PASS: ")

    while c_score < 17:
        deck_cycle += 1
        if current_card == 'A':
            card_value = 1
        elif current_card == 'J' or current_card == 'Q' or current_card == 'K':
            card_value = 10
        else: card_value = int(current_card)

        c_score += card_value
        comp_hand.append(current_card)

    print(f"Your final hand: {play_hand}, final score: {p_score}")
    print(f"Computer's final hand: {comp_hand}, final score: {c_score}")

    if p_score > 21:
        print("You busted. You Lose!!!")
    elif c_score > 21:
        print("The computer busted. You Win!!!")
    elif c_score == p_score:
        print("It's a Draw.")
    elif c_score > p_score:
        print("You Lose!!!")
    else: print("You Win!!!")

    play_again = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'n':
        exit()
    else: 
        os.system("cls")
        continue
