
# Functions with MULTIPLE Outputs
# The return in the if statement will terminate early if the "if" statement is satisfied
# Can add a note in the return to identify why it returned

first = input("Type in your first name: ")
last = input("Type in your last name: ")

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "No names were input, try again."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(first, last))
