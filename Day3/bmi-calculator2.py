# Obliczanie BMI
# 1st input: enter height in meters e.g: 1.65
height = float(input("Enter your height in meters e.g., 1.55 - "))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input("Enter your weight in kilograms e.g., 72.55 - "))
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")