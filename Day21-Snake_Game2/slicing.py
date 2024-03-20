piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[2:5])  # od 2 do 4
print(piano_keys[2:])  # od 2 do końca
print(piano_keys[:5])  # od początku do 4
print(piano_keys[2:5:2])  # od 2 do 4 co 2 pominie
print(piano_keys[::2])  # wszystko i co 2 pominie
print(piano_keys[::-1])  # odwróci listę od końca do początku
print(piano_tuple[1:])
# działa z listami jak i krotkami