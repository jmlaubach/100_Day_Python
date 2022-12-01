
import os
import random
from art import logo
from art import vs
from game_data import data

# Choose two Instagram accounts from the data dictionary

def data_shuffle(all_data):
    random.shuffle(all_data)
    return all_data

def game(first_choice, second_choice, total_score, cycle_count, new_data):
    # Print out account name, description, and location for each choice
    print(logo)
    if total_score == 0:
        pass
    else:
        print(f"You're right! Current score: {total_score}\n")
    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
    print(vs)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
    # Have the player pick a choice with 'A' or 'B'
    main_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Calculate which of the two choices has more followers
    # If wrong, exit the game.
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
    # If right, loop back to beginning and use the players choice as the next starting choice.
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


