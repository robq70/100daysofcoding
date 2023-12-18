print("Welcome to print calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
total_tip = bill * (tip / 100) + bill
bill_per_person = round(total_tip / people, 2)

# Wymuszamy pod spodem żeby python wyświetlał na końcu 2 cyfry nawet jeśli ostatnia to 0
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")