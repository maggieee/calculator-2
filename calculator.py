"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic2 import *

# Your code goes here
def is_valid(input_as_list):
    """Checks if user input is an operator followed by numbers"""
    if len(input_as_list) > 1:
        for item in input_as_list[1:]:
            if not item.isdigit():
                print("Please enter number(s) as operands")
                return False
    return True

def has_enough_arguments(args):
    """Checks if a given function has enough arguments"""

    if args[0] in ["+", "-", "*", "/", "pow", "mod"]:
        if len(args) < 3:
            print("Operator expects at least two operands. Please enter more numbers after operator.")
            return False
    elif args[0] in ["square", "cube"]:
        if len(args) != 2:
            print("Operator expects one operand. Please enter one number after operator.")
            return False
    return True

while True:
    command = input("> ")
    commands = command.split(" ")

    operator = commands[0]

    if is_valid(commands) and has_enough_arguments(commands):
        numbers = []
        for num in commands[1:]:
            numbers.append(float(num))

        if operator == "q":
            break
        elif operator == "+":
            print(add(numbers))

        elif operator == "-":
            print(subtract(numbers))

        elif operator == "*":
            print(multiply(numbers))

        elif operator == "/":
            print(divide(float(commands[1]), float(commands[2])))

        elif operator == "square":
            print(square(float(commands[1])))

        elif operator == "cube":
            print(cube(float(commands[1])))

        elif operator == "pow":
            print(power(float(commands[1]), float(commands[2])))

        elif operator == "mod":
            print(mod(float(commands[1]), float(commands[2])))

        else:
            print("Please enter a valid operator.")
