from art import logo


# Calculator
# Na początku definiujemy funkcje obliczeniowe
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Do nazw funkcji tworzymy słownik z kluczami jako operacjami, które chcemy wykonać za pomocą przypisanych do nich funkcji
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():  # Definiujemy pustą funkcję aby móc wrócić do jej początku
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_end = False

    while not should_end:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[
            operation_symbol
        ]  # przypisujemy do zmiennej nazwę danej funkcji
        answer = calculation_function(
            num1, num2
        )  # następnie przypisujemy do zmiennej z wynikiem funkcji samą funkcję wraz ze zmiennymi

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        restart = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or 'e' to exit.\n"
        )
        if restart == "y":
            num1 = answer
        elif restart == "e":
            should_end = True
        else:
            should_end = True
            calculator()  # Wywołujemy pustą funkcję aby wrócić na początek wykonywania kodu


calculator()  # Aby program zaczął działać głowna funkcja musi zostać wywołana
