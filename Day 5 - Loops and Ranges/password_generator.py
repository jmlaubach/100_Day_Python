
import random

letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
"N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", 
"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 
"r", "s", "t", "u", "v", "w", "x", "y", "z"]
numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "."]

print("Welcome to Josh's Super Strong Password Generator!")

letter_count = int(input("How many letters would you like in your password?\n"))
number_count = int(input("How many numbers wouuld you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))

final_letters = random.sample(letter, letter_count)
final_numbers = random.choices(numero, k=number_count)
final_symbols = random.sample(symbol, symbol_count)
final_list = final_letters + final_numbers + final_symbols
random.shuffle(final_list)

password = ""
for x in final_list:
    password += x
print(f"Your super strong password is: {password}")

