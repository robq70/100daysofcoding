# Obliczanie BMI
# 1st input: enter height in meters e.g: 1.65
height = float(input("Enter your height in meters e.g., 1.55 - "))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Enter your weight in kilograms e.g., 72.55 - "))

print(int(int(weight) / float(height) ** 2))
