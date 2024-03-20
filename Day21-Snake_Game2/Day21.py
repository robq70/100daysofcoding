# Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    # Klasa dziedziczy wszystko z klasy Animal
    def __init__(self):
        # super() inicjuje wszystkie metody z poprzedniej klasy
        # The call to super() in the initializer is recommended, but not strictly required.
        super().__init__()

    def breathe(self):
        # dziedziczymy metodę breathez klasy Animal - super
        super().breathe()
        # oraz dodajemy własne modyfikacje
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()
