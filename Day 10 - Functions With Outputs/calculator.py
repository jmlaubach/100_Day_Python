
import os
import art
from art import logo

# Math functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
 
operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide
}

def calculator():
    print(art.logo)
    num1 = int(input("What's the first number?: "))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        op = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calc_func = operations[op]
        answer = calc_func(num1, num2)
        print(f"{num1} {op} {num2} = {answer}")

        option = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if option == "y":
            num1 = answer
        else: 
            should_continue = False
            os.system("cls")
            calculator()

calculator()

