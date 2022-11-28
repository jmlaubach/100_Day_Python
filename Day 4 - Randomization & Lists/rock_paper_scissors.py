# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

pictures = [rock, paper, scissors]
options = ["Rock", "Paper", "Scissors"]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp_choice = random.randint(0,2)

print(pictures[choice])

print("Computer chose:")

print(pictures[comp_choice])

if choice == comp_choice:
    print("It's a Draw!")
    quit()
elif choice == 0 and comp_choice == 1:
    print("You lose!")
elif choice == 0 and comp_choice == 2:
    print("You win!")
elif choice == 1 and comp_choice == 0:
    print("You win!")
elif choice == 1 and comp_choice == 2:
    print("You lose!")
elif choice == 2 and comp_choice == 0:
    print("You lose!")
elif choice == 2 and comp_choice == 1:
    print("You win!")