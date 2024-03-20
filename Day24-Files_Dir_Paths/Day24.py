# Method open 1
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# Method open 2
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Method write mode = "r" read only, "w" write text but clear if not empty, "a" append text to file

with open("my_file.txt", mode="w") as file:
    file.write("New text.")

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# If file new_file.txt do not exist it will be created, only with mode = "w"
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")