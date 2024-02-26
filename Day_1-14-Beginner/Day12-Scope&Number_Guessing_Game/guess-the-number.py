# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from replit import clear
from art import logo

# Zmienne pisane dużą literą oznaczają globalne zmienne
EASY_LEVEL = 10
HARD_LEVEL = 5


def start_game():
    print(logo)
    end_game = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number_to_guess = randint(1, 100)
    level = input("Choose difficulty. Type 'easy' or'hard':")

    def set_difficulty():
        if level == "easy":
            return EASY_LEVEL
        else:
            return HARD_LEVEL

    attempts = set_difficulty()
    while not end_game or attempts > 0:
        attempts -= 1
        select_number = int(input("Make a guess: "))
        if select_number == number_to_guess:
            print(f"You got it! The answer was {number_to_guess}")
            end_game = True
        elif select_number > number_to_guess:
            print(
                f"Too high.\n--------------\nGuess again\nYou have {attempts} remaining to guess the number"
            )
        else:
            print(
                f"Too low.\n--------------\nGuess again\nYou have {attempts} remaining to guess the number"
            )
        if attempts == 0:
            print(f"You loose. Choosen number was: {number_to_guess}")
            end_game = True


while input("Do you want to play a game ? Type 'y' or 'n': ") == "y":
    clear()
    start_game()
