
import random
import art
from art import logo

deck = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", 
"7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", 
"Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]

deal_track = 51

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
        elif c == 'J':
            score += 10
        elif c == 'Q':
            score += 10
        elif c == 'K':
            score += 10
        else: 
            score += int(c)
    return score

def player_turn(start_score, main_deck, cc):
    score = start_score
    choice = "y"
    choice = input("Type 'y' to HIT and get another card, and type 'n' to PASS: ")
    while choice == "y":
        new_card = main_deck[cc]
        choice = input("Type 'y' to HIT and get another card, and type 'n' to PASS: ")



deck_shuffle(deck)
starting_deal = deal(deck, deal_track)

play_hand = [deal(deck, deal_track)[0], deal(deck, deal_track)[1]]
comp_hand = [deal(deck, deal_track)[2], deal(deck, deal_track)[3]]
play_score = start_score(play_hand)
comp_score = start_score(comp_hand)

print(f"Your cards: {play_hand}, current score: {play_score}")
print(f"Computers first card: {comp_hand[0]}")

player_turn(play_score, deck, deal_track)

