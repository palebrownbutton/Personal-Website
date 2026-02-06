import random
import math

def get_random(num1, num2):
    return f"Here is a random number between {num1} and {num2}: {random.randint(num1, num2)}"

def multiply(num1, num2):
    return f"{num1} times {num2} is {num1 * num2}"

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return f"{num1} divided by {num2} is {num1 / num2}"

def add(num1, num2):
    return f"{num1} plus {num2} is {num1 + num2}"

def subtract(num1, num2):
    return f"{num1} minus {num2} is {num1 - num2}"

def power(num1, num2):
    return f"{num1} to the power of {num2} is {num1 ** num2}"

def square_root(num):
    if num < 0:
        return "Error: Cannot take the square root of a negative number."
    return f"The square root of {num} is {round(math.sqrt(num), 2)}"

def factorial(num):
    if num < 0:
        return "Error: Factorial is not defined for negative numbers."
    return f"The factorial of {num} is {math.factorial(num)}"