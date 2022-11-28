
# Prints the total of all even numbers between 0-100
# The range(1, 101, 2) in the for loop means it gives a range of numbers counting up by 2 each time.

total = 0
for number in range(1, 101, 2):
    total += number

print(total)