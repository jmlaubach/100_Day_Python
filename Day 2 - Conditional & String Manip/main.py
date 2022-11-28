#If the bill was $150.00, split between 5 people, with 12% tip. 

bill = input("What is your total bill? ")
people = input("How many people are splitting the bill? ")
tip_percent = input("What percent would you like to tip? ")

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

cost = (float(bill) / int(people))
cost_round = (round(cost, 2)) 

tip_integer = float(tip_percent) / 100 
tip_round = round(tip_integer, 2)

total_tip = tip_round * cost_round
total_tip_round = round(total_tip, 2)

print(f"Your total tip for each person is: ${total_tip_round}")

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇