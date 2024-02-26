def line():
    print(
        """
          -------------------------------------------------------
          """
    )


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Wyświetlenie danych ze słownika
print(programming_dictionary["Bug"])

line()

# Dodanie nowej danej do słownika

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

line()

# Tworzenie pustego słownika
empty_dictionary = {}

line()

# Wyczyszczenie w całości pustego słownika
# programming_dictionary = {}
print(programming_dictionary)

line()

# Edytowanie danych w słowniku, jeśli nie znajdzie tego klucza utworzy go
programming_dictionary["Bug"] = "An moth in your computer."
print(programming_dictionary)

line()

# Pętla wewnątrz słownika -  w ten sposób wyświetli tylko klucze
for item in programming_dictionary:
    print(item)

line()

# Pętla wewnątrz słownika -  wyświetli klucze a pod nimi ich wartości
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
