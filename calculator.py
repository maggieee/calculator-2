"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    command = input("> ")
    command = command.split(" ")
    if command[0] == "q":
        exit()
    else:
        if command[0] == "+":
            print(add(float(command[1]), float(command[2])))

        elif command[0] == "-":
            print(subtract(float(command[1]), float(command[2])))

        elif command[0] == "*":
            print(multiply(float(command[1]), float(command[2])))

        elif command[0] == "/":
            print(divide(float(command[1]), float(command[2])))

        elif command[0] == "square":
            print(square(float(command[1])))

        elif command[0] == "cube":
            print(cube(float(command[1])))

        elif command[0] == "pow":
            print(power(float(command[1]), float(command[2])))

        elif command[0] == "mod":
            print(mod(float(command[1]), float(command[2])))

        # break

# def find_function(first):
#     if first == "+"
#         return 