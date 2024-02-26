from replit import clear
import random

from art import logo, vs
from game_data import data


def choose_card():
    return random.choice(data)


def play_game():
    print(logo)
    game_score = 0
    is_game_over = False
    type_A = choose_card()
    score_A = int(type_A["follower_count"])

    while not is_game_over:
        type_B = choose_card()
        score_B = int(type_B["follower_count"])
        print(f"You are right! Current score: {game_score}")

        print(
            "Compare A: "
            + type_A["name"]
            + ", a "
            + type_A["description"]
            + ", from "
            + type_A["country"]
        )
        print(vs)
        print(
            "Against B: "
            + type_B["name"]
            + ", a "
            + type_B["description"]
            + ", from "
            + type_B["country"]
        )
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == "a" and score_A >= score_B:
            type_A = type_B
            game_score += 1
            clear()

        elif user_choice == "b" and score_B >= score_A:
            type_A = type_B
            game_score += 1
            clear()
        else:
            clear()
            print(logo)
            print(f"Sorry, that is wrong! Final score: {game_score}")
            is_game_over = True


play_game()
