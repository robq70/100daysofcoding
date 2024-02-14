# Input a list of student scores
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"The highest score in the class is: {high_score}")

# Aby uwzglednił liczbę 10 musimy poać zakres o 1 więcej
for number in range(1, 11, 3):
    print(number)

# Sumuje cyfry od 1-100
total = 0
for number in range(1, 101):
    total += number
print(total)
