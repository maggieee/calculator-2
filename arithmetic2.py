"""Math functions for calculator."""


def add(numbers):
    """Return the sum of the inputs."""
    return sum(numbers)


def subtract(numbers):
    """Return the subsequent numbers subtracted from the first."""
    total = numbers[0]
    for i in numbers[1:]:
        total -= i

    return total


def multiply(numbers):
    """Multiply the inputs together."""
    product = 1
    for i in numbers:
        product *= i

    return product


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    return num1/num2


def square(num1):
    """Return the square of the input."""
    return num1*num1


def cube(num1):
    """Return the cube of the input."""
    return num1*num1*num1


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1**num2


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1 % num2


def add_mult(num1, num2, num3):
    """Returns the sum of the first two inputs multiplied by the third"""
    return (num1 + num2) * num3


def add_cubes(num1, num2):
    """Returns the sum of the cubes of the two inputs"""
    return cube(num1) + cube(num2)