import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
select_object = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if user_choice >= 3 or user_choice < 0:
    print("Computer Paper wins")
else:
    print(select_object[user_choice])
computer_choice = random.randint(0, 2)
print("Computer choice:")
print(select_object[computer_choice])
if user_choice == 0 and computer_choice == 1:
    print("Computer Paper wins")
elif computer_choice == 0 and user_choice == 1:
    print("User Paper wins")
elif user_choice == 1 and computer_choice == 2:
    print("Computer Scissors wins")
elif computer_choice == 1 and user_choice == 2:
    print("User Scissors wins")
elif user_choice == 2 and computer_choice == 0:
    print("Computer Rock wins")
elif computer_choice == 2 and user_choice == 0:
    print("User Rock wins")
else:
    print("It's draw")
