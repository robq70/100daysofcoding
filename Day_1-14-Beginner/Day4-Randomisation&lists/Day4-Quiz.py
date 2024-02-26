"""
Given the code below:
What do you think will be printed?
"""

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

# Return - ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Melons', 'Lemons']


"""
Given the code below:
What do you think will be printed?
"""
fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
