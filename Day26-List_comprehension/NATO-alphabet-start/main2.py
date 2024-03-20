import pandas
data = pandas.read_csv("day-25-end/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = data.to_dict()
print(data_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.