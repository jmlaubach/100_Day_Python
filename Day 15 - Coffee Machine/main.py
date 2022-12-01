
from machine_data import coffee_data
from machine_data import coin_data

# Print report on resources if needed

def report(d_choice, water_l, milk_l, coffee_l, money_l):
    '''Prints out a report of each resource in the coffee maker.'''
    print(f"Water: {water_l}ml")
    print(f"Milk: {milk_l}ml")
    print(f"Coffee: {coffee_l}g")
    print(F"Money: ${money_l}")

def resource_calc(drink, water_l, milk_l, coffee_l, drink_data):
    '''Takes the "drink_choice" of the user and pulls the required ingredient amounts from data.
    It compares those amounts to the levels of the coffee machine and decides if there isn't enough.'''
    if drink_data[drink.title()]['ingredients']['water'] > water_l:
        print("Sorry, there is not enough water.")
        coffee_machine()
    elif drink_data[drink.title()]['ingredients']['milk'] > milk_l:
        print("Sorry, there is not enough milk.")
        coffee_machine()
    elif drink_data[drink.title()]['ingredients']['coffee'] > coffee_l:
        print("Sorry, there is not enough coffee.")
        coffee_machine()
    else: return

def money_calc(coins):
    '''Calculates total the user spent based on coins inserted into the machine.
    Checks total for each coin against value from the machine_data dictionary.'''
    print("Please insert coins.")
    q_tot = (int(input("How many quarters?: ")) * coins['Quarter'])
    d_tot = (int(input("How many dimes? ")) * coins['Dime'])
    n_tot = (int(input("How many nickels? ")) * coins['Nickel'])
    p_tot = (int(input("How many pennies? ")) * coins['Penny'])
    tot_coin_spent = q_tot + d_tot + n_tot + p_tot
    return tot_coin_spent

def make_drink(drinks, d_choice, water_l, milk_l, coffee_l, money_l):
    '''Makes an espresso for the user and dispenses appropriate change.
    Updates resources in coffee machine based on espresso ingredient values.'''
    drink_cost = drinks[d_choice.title()]['cost']
    choice = d_choice.title()
    money_inserted = money_calc(coin_data)
    if money_inserted > drink_cost:
        water_l -= drinks[choice]['ingredients']['water']
        milk_l -= drinks[choice]['ingredients']['milk']
        coffee_l -= drinks[choice]['ingredients']['coffee']
        money_l += drinks[choice]['cost']
        change = money_inserted - drink_cost
        print(f'Here is ${change:.2f} in change.')
        print(f"Here is your {choice}. Enjoy!")
    else:
        print("Not enough. Please insert more coins.")

def coffee_machine():
    drink_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if drink_choice == 'report':
        report(water_level, milk_level, coffee_level, money_level)
    else:
        make_drink(coffee_data, drink_choice, water_level, milk_level, coffee_level, money_level)
    #elif drink_choice == 'latte':
    #elif drink_choice == 'cappuccino':

# Confirm resources are sufficient
## Prompt to add resources if more are needed

# Ask to insert coins (how many of each type)
# Calculate if total inserted is enough for drink, if so, dispense drink
# calculate difference over and dispense change back to user

# Return to prompt for drink choice

water_level = 300
milk_level = 200
coffee_level = 100
money_level = 0

coffee_machine()
