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
            print(add(int(command[1]), int(command[2])))

# def find_function(first):
#     if first == "+"
#         return 