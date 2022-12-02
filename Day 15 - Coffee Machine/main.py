
from machine_data import coffee_data
from machine_data import coin_data

# Print report on resources if needed

def report(water_l, milk_l, coffee_l, money_l):
    '''Prints out a report of each resource in the coffee maker.'''
    print(f"Water: {water_l}ml")
    print(f"Milk: {milk_l}ml")
    print(f"Coffee: {coffee_l}g")
    print(F"Money: ${money_l}")

def resource_calc(drink, water_l, milk_l, coffee_l, drink_data):
    '''Takes the "drink_choice" of the user and pulls the required ingredient amounts from data.
    It compares those amounts to the levels of the coffee machine and decides if there isn't enough.
    When all resources are satisfied, returns to machine order.'''
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
    Checks total for each coin against value from the machine_data dictionary.
    Returns total amount put into the machine.'''
    print("Please insert coins.")
    q_tot = (int(input("How many quarters?: ")) * coins['Quarter'])
    d_tot = (int(input("How many dimes? ")) * coins['Dime'])
    n_tot = (int(input("How many nickels? ")) * coins['Nickel'])
    p_tot = (int(input("How many pennies? ")) * coins['Penny'])
    tot_coin_spent = q_tot + d_tot + n_tot + p_tot
    return tot_coin_spent

def refill_check(drinks, d_choice, wl, ml, cl):
    '''Checks if resource is too low to make the required drink.
    Calculates and returns the difference from current to maximum.'''
    if wl < drinks[d_choice.title()]['ingredients']['water']:
        return "+water"
    elif ml < drinks[d_choice.title()]['ingredients']['milk']:
        return "+milk"
    elif cl < drinks[d_choice.title()]['ingredients']['coffee']:
        return "+coffee"



def make_drink(drinks, d_choice):
    '''Makes an drink for the user and dispenses appropriate change.
    Uses the drink choice to find the key in the dictionary and pull values.
    Creates drink and updates all resources in the coffee machine appropriately.'''
    global water_level
    global milk_level
    global coffee_level
    global money_level
    drink_cost = drinks[d_choice.title()]['cost']
    choice = d_choice.title()
    cost = drinks[d_choice.title()]['cost']
    print(f"{choice} costs ${cost:.2f}.")
    money_inserted = money_calc(coin_data)
    while money_inserted < drink_cost:
            print(f"You have inserted ${money_inserted:.2f}")
            print("Not enough.")
            money_inserted += money_calc(coin_data)

    water_level -= drinks[choice]['ingredients']['water']
    milk_level -= drinks[choice]['ingredients']['milk']
    coffee_level -= drinks[choice]['ingredients']['coffee']
    money_level += drinks[choice]['cost']
    change = money_inserted - drink_cost
    print(f'Here is ${change:.2f} in change.')
    print(f"Here is your {choice}. Enjoy!")


def coffee_machine():
    '''Contains main code to run through machine steps and perform all checks.
    Returns to prompting for drink after going through steps and delivering drink.'''
    global water_level
    global milk_level
    global coffee_level
    drink_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if drink_choice == 'report':
        report(water_level, milk_level, coffee_level, money_level)
        coffee_machine()
    else:
        while water_level < coffee_data[drink_choice.title()]['ingredients']['water'] or milk_level < coffee_data[drink_choice.title()]['ingredients']['milk'] or coffee_level < coffee_data[drink_choice.title()]['ingredients']['coffee']:
            print("Insufficient ingredients.") 
            if refill_check(coffee_data, drink_choice, water_level, milk_level, coffee_level) == "+water":
                input("To refill water, hit 'Enter': ")
                water_level += (300 - water_level)
            elif refill_check(coffee_data, drink_choice, water_level, milk_level, coffee_level) == "+milk":
                input("To refill milk, hit 'Enter': ")
                milk_level += (200 - milk_level)
            else:
                input("To refill coffee, hit 'Enter': ")
                coffee_level += (100 - coffee_level)
        make_drink(coffee_data, drink_choice)
    coffee_machine()

water_level = 300
milk_level = 200
coffee_level = 100
money_level = 0

coffee_machine()
