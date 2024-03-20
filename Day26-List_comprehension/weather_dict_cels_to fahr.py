weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {temp_c: degree * 9 / 5 + 32 for (temp_c, degree) in weather_c.items()}

print(weather_f)
