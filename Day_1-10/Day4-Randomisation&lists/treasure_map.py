line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "B3"  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# Zamieniamy pierwszy znak na małe litery
letter = position[0].lower()

# tworzymy listę do porównania
abc = ["a", "b", "c"]

# spawdzamy którą pozycję na liście w indeksie zajmuje dana w letter
letter_index = abc.index(letter)
print(letter_index)

# spawdzamy którą pozycję na liście w indeksie zajmuje druga dana w position - odejmujemy 1 ponieważ 3 to na liście 2
number_index = int(position[1]) - 1
print(number_index)

# wpisujemy x na podstawie odczytanych pozycji number_index i letter_index
map[number_index][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
