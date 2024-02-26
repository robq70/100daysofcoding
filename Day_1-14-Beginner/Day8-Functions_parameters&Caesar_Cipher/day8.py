def line():
    print(
        """
          -------------------------------------------------------
          """
    )


def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


greet()

line()


def greet_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today {name}?")


greet_name("Robert")

line()


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Robert", "Zawiercie")

line()


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with(location="Zawiercie", name="Robert")
