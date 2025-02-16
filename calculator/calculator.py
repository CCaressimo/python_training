"""Calculator application"""

from os import system

def add(n1, n2):
    """add function"""
    return n1 + n2

def subtract(n1, n2):
    """subtract function"""
    return n1 - n2

def multiply(n1, n2):
    """multiply function"""
    return n1 * n2

def divide(n1, n2):
    """divide function"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """Calculator function"""
    CALCULATE = True
    n1 = int(input("What's the first number?\n"))

    while CALCULATE:

        operation_input = input("Pick an operation\n+\n-\n*\n/\n")
        n2 = int(input("What's the second number?\n"))
        result = operations[operation_input](n1,n2)
        print(f"{n1} {operation_input} {n2} = {result}")

        continue_operation = input(f"Type 'y' to continue calculating with {result}"
                                f", or type 'n' to start a new calculation, "
                                "or type 'stop' to turn off the calculator:\n").lower()

        if continue_operation == "y":
            n1 = result
            result = operations[operation_input](n1,n2)
            print(f"{n1} {operation_input} {n2} = {result}")
        elif continue_operation == "stop":
            CALCULATE = False
        else:
            CALCULATE = False
            system("clear")
            calculator()

calculator()
