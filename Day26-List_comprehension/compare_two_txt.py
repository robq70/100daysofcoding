with open("file1.txt") as file1_txt:
    file1 = []
    for names in file1_txt:
        names = names.strip(",\n")
        file1.append(names)

with open("file2.txt") as file2_txt:
    file2 = []
    for names in file2_txt:
        names = names.strip(",\n")
        file2.append(names)
result = [int(num) for num in file1 if num in file2]
print(file1)
print(file2)
print(result)

# Second method
with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

# Your code above 👆
print(list1)
print(list2)
print(result)
