# Step 1: Choose a word randomly from list

# Step 2: Ask user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# Step 3: Check if letter is of of the letters in the chosen word.

import random
import hangman_art
import hangman_words
from hangman_art import logo, stages

print(hangman_art.logo)

word_list = ["aardvark", "baboon", "camel"]
w = list(random.choice(hangman_words.word_list))
length = len(w)
blanks = []
start = ["_"]
blanks.extend(start * length)
lives = 6

def guess():
    guess.letter = input("Guess a letter: ").lower()
    print(guess.letter)

def game():
    global lives
    if guess.letter in w:
        for count, value in enumerate(w):
            if value == guess.letter:
                blanks[count] = guess.letter
            else: pass
    else: lives -= 1
    print(hangman_art.stages[lives])
    print(f'''{blanks}

    You have {lives} guesses left\n''')

while w != blanks:
    if lives > 0:
        guess()
        game()
    else:
        print("You are out of guesses. Game over!\n")
        print("Your word was: " + "".join(w))
        quit()

print("You have won!")
