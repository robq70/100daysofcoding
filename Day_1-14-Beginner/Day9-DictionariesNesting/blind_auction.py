from replit import clear
from art import logo

print(logo)


bids = {}


def add_new_offer(client_name, offer_amount):
    bids[client_name] = offer_amount


should_end = False

while not should_end:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    add_new_offer(name, price)

    restart = input("Are there any other bidders. Type 'yes' or 'no'.\n")
    if restart == "no":
        highest_value = 0
        for key in bids:
            new_value = bids[key]
            if new_value > highest_value:
                highest_value = new_value
                winner = key
        should_end = True
        clear()
        print(f"The winner is {winner} with a bid of ${highest_value}")
    else:
        clear()
