# Simple function
def greet():
    print("Isn't the weather nice today?")

greet()

# Function that allow for input

def greet_with_name(name):
    print(f"Isn't the weather nice today {name}?")

greet_with_name("Piper")

# Function that allows for MULTIPLE inputs

def greet_with(name, location):
    print(f"Hello {name}! What is it like in {location} today?")

greet_with("Franklin", "Hell")