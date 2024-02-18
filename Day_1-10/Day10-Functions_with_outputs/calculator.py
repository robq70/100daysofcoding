from replit import clear
from art import logo


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    should_end = False
    while not should_end:
        print("+\n-\n*\n/")
        operation = input("Pick an operation?: ")
        num2 = float(input("What's the next number?: "))

        def math_operations(num1, num2):
            if operation == "+":
                return num1 + num2
            elif operation == "-":
                return num1 - num2
            elif operation == "*":
                return num1 * num2
            else:
                return num1 / num2

        result = math_operations(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        restart = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.\n"
        )
        if restart == "y":
            num1 = result
        elif restart == "n":
            should_end = True
            calculator()
        else:
            should_end = True


calculator()
