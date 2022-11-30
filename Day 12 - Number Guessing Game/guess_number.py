
import random
import art
from art import logo


def guess_loop(guesses):
    global number
    remainder = guesses
    while remainder > 0:
        print(f"You have {remainder} guesses remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            quit()
        elif guess > number:
            remainder -= 1
            print("Too high.")
            print("Guess again.")
        else:
            remainder -= 1
            print("To low.")
            print("Guess again.")
    print("You ran out of guesses. You lose!")
    print(f"The number was {number}")


print(logo)
print("Welcome to the Number Guessing Game!")

number = random.randint(1, 100)
print("I'm think of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard' to choose: ")
if choice == 'easy':
    total_guesses = 10
    guess_loop(total_guesses)
else: 
    total_guesses = 5
    guess_loop(total_guesses)