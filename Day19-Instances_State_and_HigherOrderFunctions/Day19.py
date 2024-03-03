def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    # higher order function
    return func(n1, n2)

# call to higher order function
result = calculator(2, 3, add)
print(result)
