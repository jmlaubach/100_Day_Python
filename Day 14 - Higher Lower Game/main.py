
import os
import random
from art import logo
from art import vs
from game_data import data

def data_shuffle(all_data):
    random.shuffle(all_data)
    return all_data

def game(first_choice, second_choice, total_score, cycle_count, new_data):
    print(logo)
    if total_score == 0:
        pass
    else:
        print(f"You're right! Current score: {total_score}\n")
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
    print(vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
    main_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if main_choice == 'a':
        main_choice = first_choice
        if main_choice['follower_count'] < second_choice['follower_count']:
            print(f"Sorry, that's wrong. Final score: {total_score}")
            quit()
        else:
            total_score += 1
    else:
        main_choice = second_choice
        if main_choice['follower_count'] < first_choice['follower_count']:
            print(f"Sorry, that's wrong. Final score: {total_score}")
            quit()
        else:
            total_score += 1
    first_choice = second_choice
    cycle_count += 1
    second_choice = new_data[cycle_count]
    if cycle_count <= 51:
        os.system("cls")
        game(first_choice, second_choice, total_score, cycle_count, new_data)
    else:
        print(f"You have correctly guessed all comparisons! Your final score: {total_score}")
        quit()


starting_data = data_shuffle(data)
choice_a = data[0]
choice_b = data[1]
list_cycle = 1
score = 0

game(choice_a, choice_b, score, list_cycle, starting_data)

# NOTES

# Could add small improvement to change 'a' to 'an' in the comparison statement if the 
# description of the account starts with a vowel.

# Would be cool to change this to actually pull a random account from Instagram itself
# with over 1 mil followers and compare it to another account instead of using the list.

# There is some repetition in the code. Some of it could be consolidated into other 
# functions to reduce redundancy.


