
# Object Oriented Programming (OOP)

# Object is made up of 'attributes' and 'methods'
    # attributes are variables associated with an object, and attached to that object
    # methods are functions that modeled objects can do and use

# Think of it as like modeling real life objects
# If you were to model a waiter and create an object:
    # attributes are what the waiter has
    # methods are what the waiter does

# Class: The main type for a job in a program (car)
# Objects: Individual objects generated from this main class blueprint (types of cars)
# car = CarBlueprint()
    # CarBlueprint is the class. First letter of each word is capitalized to differentiate it
    # car is the object, created from the CarBlueprint() class

# turtle module example using classes

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()