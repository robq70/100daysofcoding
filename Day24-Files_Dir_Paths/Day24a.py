# File on other HDD than working directory
with open('C:/Users/robq7/Desktop/my_file.txt') as file:
    contest = file.read()
    print(contest)

# File on the same HDD where is working directory but outside it
with open('/Git_folder/my_file.txt') as file:
    contest = file.read()
    print(contest)

# File is in D:\Git_folder\
with open('../../my_file.txt') as file:
    contest = file.read()
    print(contest)
