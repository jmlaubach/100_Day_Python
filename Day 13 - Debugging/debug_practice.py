
############DEBUGGING#####################

# Each section will have starting broken code followed by debugged
# solution depending on what is required to fix it.

# Describe Problem
# The for loop won't include the last number in the range
# Need to change 20 to 21 to include 20 in the range
def my_function():
    # for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it")
my_function()

# Reproduce the Bug
# randint includes both endpoints of the range
# Because the "dice_imgs" list goes from 0-5, when 6 is chosen, it is out of the range
# Need to change randint to: randint(0, 5)
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
# There is no >= or <= in the if statement
# This means the year 1994 won't be checked at all and output nothing
# Need to set the Gen Z elif statement to be year >= 1994 instead of just >
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
#elif year > 1994:
elif year >= 1994:
    print("You are a Gen Z.")

# # Fix the Errors
# print is not indented under the if statement
# there also needs to be an f in front of the first quote to format the f string properly
# the age input needs to be changed to an integer to be compared to 18

#age = input("How old are you?")
age = int(input("How old are you? "))
if age > 18:
#print("You can drive at age {age}.")
    print(f"You can drive at age {age}.")

# #Print is Your Friend
# the == in 4th line needs to just be an = sign instead
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
#word_per_page == int(input("Number of words per page: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# The b_list.append hasn't been included in the for loop
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    #b_list.append(new_item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])