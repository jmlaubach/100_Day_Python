
# List looks like this: variable = ["item1", "item2", "item3"]

import random

states = ["Virginia", "Maryland", "Delaware"]

print(states[random.randint(0, 2)])

# Edit and change the specified item in the list
states[2] = "Delastupid"

# Adds an item to the end of the list
# Many more functions then this in documentation for list
states.append("North Carolina")

print(states)