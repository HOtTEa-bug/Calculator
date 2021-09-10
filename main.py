import os

# Calculator
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

# Division
def div(n1, n2):
    return n1 / n2

# Dictionary for operations
Operations = {
    "+": add, 
    "-": sub, 
    "*": mul, 
    "/": div
    }

# calculator function
def calculator():
    os.system("cls")
    print(logo)

    num1 = float(input("Enter the first number: "))
    for symbol in Operations:
        print(symbol )
    should_continue = True

    while should_continue:
        Operation_symbol = input("Pick an operation from the above list: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = Operations[Operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {Operation_symbol} {num2} = {answer}")


        command = input(f"Type 'y' to continue calculating with {answer}; or 'c' to start a new calculation; or 'n' to end operations: ")

        if command == "y":
            num1 = answer
        elif command == "c":
            should_continue = False
            calculator() #recursion
        else:
            should_continue = False

calculator()

