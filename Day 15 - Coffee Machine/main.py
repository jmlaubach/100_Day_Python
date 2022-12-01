
from machine_data import coffee_data
from machine_data import coin_data

# Print report on resources if needed

def user_choice():

def resource_check(drinks, coins):
    
def report(water, milk, coffee, money):
    '''Prints out a report of each resource in the coffee maker.'''
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(F"Money: ${money}")

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

def espresso_make(drinks, water_l, milk_l, coffee_l, money_l):
    '''Makes an espresso for the user and dispenses appropriate change.
    Updates resources in coffee machine based on espresso ingredient values.'''
    esp_cost = drinks['Espresso']['cost']
    if money_calc(coin_data) > esp_cost:
        water_l -= drinks['Espresso']['ingredients']['water']
        milk_l -= drinks['Espresso']['ingredients']['milk']
        coffee_l -= drinks['Espresso']['ingredients']['coffee']
        money_l += drinks['Espresso']['ingredients']['water']
        change = money_calc(coin_data) - esp_cost
    else:
        print("Not enough. Please insert more coins.")
    

#def latte_make():

#def cappuccino_make():

def coffee_machine():
    # Ask for drink choice
    drink_choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if drink_choice == 'report':
        report(water_level, milk_level, coffee_level, money_level)
    elif drink_choice == 'espresso':
        espresso_make(coffee_data, water_level, milk_level, coffee_level, money_level)
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
