# For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
new_list = [n + 1 for n in numbers]

# String as List
name = "Angela"
letters_list = [letter for letter in name]

# Range as List
range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension
import random

student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)

student_dict = {"student": ["Alex", "Beth", "Angela"],
                "score": [56, 76, 98]}
# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)
#     print(key)

# Pandas Dictionary Comprehension
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a data frame:
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Looping through rows of data frame:
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print(row.score)
