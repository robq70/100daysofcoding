# Data types
# String
print("Hello"[4])
print("123" + "345")

# Integer
print(123 + 345)

# Można napisać jak poniżej aby lepiej zrozumieć większe cyfry a system zinterpretuje to jako 123456789
print(123_456_789)


# Float
3.14159

# Boolean
True
False

# num_char = len(input("What is your name\n"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# type pokazuje nam z jakiego rodzaju danymi mam do czynienia
a = str(123)
print(type(a))

# Pierwsze doda nam cyfry drugie połączy tekst
print(70 + float("100.5"))
print(str(70) + str(100))

# 3 + 5
# 7 - 5
# 3 * 5
# 6 / 3
# 2**3
#       PEMDAS
# Parentheses     Nawiasy ()
# Exponents       Potęgi **
# Multiplication  Mnożenie * Division        Dzielenie /
# Addition        Dodawanie +  Subtraction     Odejmowanie -

# Kolejność działań na liczbach
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# Obetnie cyfry po przecinku i będzie 2
print(int(8 / 3))

# Zaokrągli do najbliższej cyfry po przecinku i będzie 3
print(round(8 / 3))

# Pokaże wynik z dwoma cyframi po przecinku i będzie 2,67
print(round(8 / 3, 2))

# Obetnie cyfry po przecinku i będzie 2
print(8 // 3)


# Działania na zmiennych
result = 4 / 2
result /= 2
print(result)


score = 0
# User scores a point
# score = score + 1
score += 1
print(score)

# F-strings nie trzeba konwertować podczas wyświetlania wyniku operacji
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
