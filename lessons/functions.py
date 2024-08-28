"""Practice with Functions"""

from random import randint

print(randint(3, 17))


# Defining a function for a sum of two numbers
def sum(num1: int, num2: int) -> int:
    """Return the sum of num1 and num2."""
    return num1 + num2


# Calling the summation function
print(sum(num1=2, num2=13))  # <- arguments


# Defining a function for a remainder of two numbers
def remainder(num1: int, num2: int) -> int:
    """Return the remainder when you divide two numbers"""
    return num1 % num2


# Calling the remainder function
print(remainder(num1=20, num2=8))  # <- arguments


# Defining a function to multiply two numbers
def multiply(num1: int, num2: int) -> int:
    return num1 * num2


# Calling the multiply function to multiply two random numbers between 1 and 100
print(multiply(num1=randint(1, 100), num2=randint(1, 100)))
