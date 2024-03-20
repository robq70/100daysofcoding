def add(*args):
    print(args[0])
    print(type(args))  # class tuple
    print(args)
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 4, 5, 6))


# def calculate(**kwargs):
#     print(type(kwargs)) # class dict
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["add"])
#
#
# calculate(add=3, multiply=5)


def calculate(n, **kwargs):
    n += kwargs["add"]  # 2+3=5, n=5
    n *= kwargs["multiply"]  # 5*5=25
    print(n)


calculate(2, add=3, multiply=5)


# class Car:
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
#
# my_car = Car(make="Nissan",model="GT-R") # If we miss some argument we get error code
# print(my_car.make)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
