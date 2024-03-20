with open('Input/Names/invited_names.txt') as file:
    invited_names = []
    for names in file:
        names = names.strip(",\n")
        invited_names.append(names)
with open('Input/Letters/starting_letter.txt') as file_doc:
    contents = file_doc.read()
    for name in invited_names:
        new_content = contents.replace("[name]", name)
        new_file_name = f"{name}.txt"
        with open(f"./Output/ReadyToSend/ReadyToSend_{new_file_name}", mode="a") as complete_file:
            complete_file.write(new_content)
