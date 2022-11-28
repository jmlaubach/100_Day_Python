

print("Hello, welcome to our roller coaster!")
print("You have to be a certain height to ride.")

height = float(input("What is your height in centimeters? "))

if height > 120:
    age = int(input("Great, you can ride! How many years old are you? "))
    if age < 12:
        print("Your ride ticket will be $5.")
    elif age <= 18:
        print("Your ride ticket will be $7.")
    else:
        print("Your ride ticket will be $9.")
else: 
    print("Unfortunately you aren't tall enough to ride. Come back next year!")