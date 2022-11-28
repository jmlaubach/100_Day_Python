
# You MUST put the "FizzBuzz" statement first 
# This is because if it finds the number is divisible by 3 or 5, it will skip to the next number.
# The "FizzBuzz" check won't get done if it isn't checked first

for n in range(1, 101): 
  if n % 3 == 0 and n % 5 == 0:
    n = "FizzBuzz"
    print(n)
  elif n % 5 == 0:
    n = "Buzz"
    print(n)
  elif n % 3 == 0:
    n = "Fizz"
    print(n)
  else: 
    n = n
    print(n)

  