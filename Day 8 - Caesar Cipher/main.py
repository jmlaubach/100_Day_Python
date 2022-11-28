
import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#alpha_shifted = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
#'m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#def encrypt(shift):
#    for x in range(0, 26):
#        if x <= (25 - shift):
#            alpha_shifted[x] = alphabet[(x + 3)]
#        else:
#            alpha_shifted[x] = alphabet[(x - 26) + shift]
#    print(alpha_shifted)

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)   
        if position <= (25 - shift_amount):
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            new_position = (position - 26) + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")

def decrypt(secret, shift_amount):
    plain_text = ""
    for letter in secret:
        position = alphabet.index(letter)
        if position >= (0 + shift_amount):
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            new_position = (position + 26) - shift_amount
            new_letter = alphabet[new_position]
            plain_text += new_letter
    print(f"The encoded text is: {plain_text}")

while True:
    option = input("Type 'encrypt to encrypt, type 'decrypt' to decrypt:\n")
    code = (input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    if option == "encrypt":
        encrypt(plain_text=code, shift_amount=shift)
    else: decrypt(secret=code, shift_amount=shift)

    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer == "yes":
        continue
    else: break


