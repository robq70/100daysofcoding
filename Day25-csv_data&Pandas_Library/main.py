# Method 1

# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# Method 2 using csv
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Method 3 using Pandas
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
# Average of temperature using python methods
avg_temp = sum(temp_list) / len(temp_list)
print(round(avg_temp, 2))
# Average of temperature using pandas methods
print(data["temp"].mean())
# Max of temperature using pandas methods
print(data["temp"].max())

# Get data in columns - both the same effects
print(data["condition"])
print(data.condition)

# Get data in row - both the same effects
print("Monday day --------------------------")
print(data[data["day"] == "Monday"])
print(data[data.day == "Monday"])
print("Day with highest temperature--------------------------")
print(data[data.temp == data["temp"].max()])
print(data[data.temp == data.temp.max()])

# When we add Monday to variable monday we can refer to row inside data of monday using names of columns
print("Refer directly to Monday --------------------------")
monday = data[data.day == "Monday"]
print(monday.condition)
print("Convert Monday temp C to F----------------------------")
print(monday.temp * 9 / 5 + 32)
# Create a dataframe from scratch
data_dict = {"students": ["Amy", "Alma", "Angela"],
             "scores": [76, 56, 65]}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
