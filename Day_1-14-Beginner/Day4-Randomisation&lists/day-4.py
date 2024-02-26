# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

states_of_america = ["Alaska","Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# print(states_of_america[34])
# print(states_of_america[-1])

# # W liście można zmienić nazwę danej dynamicznie odwołując się do niej np. zamiast Arizona na tej pozycji zobaczymy Agrisona
# states_of_america[1] = "Agrisona"

# # W liście można również dodać nową nazwę np. Lalaland
# states_of_america.append("Lalaland")

# # Listę można również rozszerzyć o inną listę np. Billland, Openland
# states_of_america.extend(["Billland", "Openland"])

# Aby nie przekroczyć / przeoczyć zakresu listy możemy ją policzyć. Ponieważ len liczy od 1 a nie od 0 musimy odjąć 1
num_of_states = len(states_of_america)

print(states_of_america[num_of_states - 1])

# Lista warzyw i owoców zanieczyszczonych pestycydami
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Możemy stworzyć osobne listy np. owoce i warzywa a później utworzyć za ich pomocą listę dirty_dozen

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# Jeśli teraz wyświetlimy listy to będą one wyglądały tak [['Owoce', 'xx'],['Warzywa', 'yy']]
dirty_dozen [fruits, vegetables]

# Wyświetlanie [1][2] i [1][3] - oznacza że wyświetli z zagnieżdżonych list pozycję 3 oraz 4 na drugiej liście (pamiętaj liczymy od 0!)
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

# Wyświetlanie [0] - oznacza że wyświetli z zagnieżdżonych list całą ppierwszą listę (pamiętaj liczymy od 0!)
print(dirty_dozen[0])