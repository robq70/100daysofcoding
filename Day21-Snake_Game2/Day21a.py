# Given this:
class Dog:
    def __init__(self):
        self.temperament = "loyal"

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


# What will this code print?

doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")