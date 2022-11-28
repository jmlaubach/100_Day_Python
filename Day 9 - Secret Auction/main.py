
import os
import art
from art import logo

#dictionary = {
#   "bidder_1": {"name": "John", "bid": "130"},
#   "bidder_2": {"name": "Mary", "bid": "125"},
#   "bidder_3": {"name": "Fred", "bid": "150"},
#} 

count = 0
bid_dict = {}
temp_dict = {}

# Could have set a dictionary by getting name, price, then doing dic_name[name] = price
# Also seemed to have made the nested dictionary as a needless complicated step.
# Could have just done a single dictionary with {name: bid, name: bid}

def bidding(dict_bid=bid_dict, dict_temp=temp_dict, dict_entry=count):
    cont = ("yes")
    while cont == "yes":
        name_temp = input("What is your name?: ")
        bid_temp = int(input("What's your bid?: ").replace("$",""))

        dict_entry += 1
        dict_temp = dict(name = name_temp, bid = bid_temp)
        dict_bid["bidder_" + (str(dict_entry))] = dict_temp
        dict_temp = {}
        
        cont = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        os.system("cls")

def winner(dict_bid=bid_dict):
    amount = 0
    name = ""
    for key in dict_bid:
        if int(dict_bid[key]['bid']) > int(amount):
            amount = dict_bid[key]['bid']
            name = dict_bid[key]['name']
        else: pass
    os.system("cls")
    print(f"The winner is {name} with a bid of {amount}.")
    #name = 
    #bid = 
    #print(f"The winner is {name} with a bid of {bid}.")

print(art.logo)
print("Welcome to the secret auction program.")

bidding()
winner()


