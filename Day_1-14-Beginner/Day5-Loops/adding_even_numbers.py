target = int(
    input("Enter a number between 0 and 1000:")
)  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total_even = 0
if target > 1000:
    target = 1000
for number in range(1, target + 1):
    if number % 2 == 0:
        total_even += number
print(total_even)


# Drugi sposób
even_sum = 0
for number in range(2, target + 1, 2):
    even_sum += number
print(even_sum)
