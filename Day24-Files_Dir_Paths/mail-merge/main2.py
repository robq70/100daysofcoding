PLACEHOLDER = "[name]"
with open('Input/Names/invited_names.txt') as file:
    invited_names = file.readlines()

with open('Input/Letters/starting_letter.txt') as file_doc:
    contents = file_doc.read()
    for name in invited_names:
        name = name.strip(",\n")
        new_content = contents.replace(PLACEHOLDER, name)
        new_file_name = f"{name}.txt"
        with open(f"./Output/ReadyToSend/letter_for_{new_file_name}", mode="a") as complex_file:
            complex_file.write(new_content)
