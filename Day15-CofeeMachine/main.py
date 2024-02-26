from cofee_data import MENU, resources


def data_coffee(choose):
    order = MENU[choose]["ingredients"]
    if resources["water"] <= order["water"] and resources["milk"] <= order["milk"] and resources["coffee"] <= order["coffee"]:
        return True
    else:
        print("Sorry there is not enough ingredients")


def calc_payment(total, coffee):
    coffe_cost = MENU[coffee]["cost"]
    order = MENU[coffee]["ingredients"]
    if total >= coffe_cost:
        change = round(total-coffe_cost, 2)
        water = resources["water"] - order["water"]
        milk = resources["milk"] - order["milk"]
        coffee = ["coffee"] - order["coffee"]
        money = money + coffe_cost
        print(f"Here is your {coffee}. Enjoy!.")
        print(f"Your change = ${change}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def report(water, milk, coffee, money):
    print(f"water = {water}ml\nmilk = {milk}ml\ncoffee = {coffee}g\nmoney = ${money}")


end_of_prepare = False
money = 0
while not end_of_prepare:
    coffee_choose = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_choose == "off":
        end_of_prepare = True
        print("Off")
    elif coffee_choose == "report":
        report(water, milk, coffee, money)
    else:
        if data_coffee(coffee_choose):
            total = input("How many quarters?: ") * 0.25
            total += input("How many dimes?: ") * 0.10
            total += input("How many nickles?: ") * 0.05
            total += input("How many pennies?: ") * 0.01
            total = (total, 2)
            if calc_payment(total, coffee_choose):
                print("Here is your coffee")
make_coffee()