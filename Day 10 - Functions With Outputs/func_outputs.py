
# Functions with Outputs
# The 'return' word will mark the end of the function and exit it. 
# No lines afterwards in the function will execute

first = input("Type in your first name: ")
last = input("Type in your last name: ")

def format_name(f_name, l_name):
    """This docstring is like a comment, and is used only for documentation in a function."""
    full_name = (f"{f_name} {l_name}").title()
    #print(full_name)
    return full_name

print(format_name(first, last))
print(len(format_name(first, last)))
