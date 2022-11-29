# Scope Notes

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Can only call the nested drink_potion() function from within the game() function
# because it was created within that function.
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    
    drink_potion()
