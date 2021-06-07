from data import MENU


def coins_summed(_pennies, _nickles, _dimes, _quarters):
    return _pennies * 0.01 + _nickles * 0.05 + _dimes * 0.1 + _quarters * .25


def make_drink(_choice, _resources):
    new_water = _resources["water"] - MENU[_choice]["ingredients"]["water"]
    if _choice == "espresso":
        new_milk = _resources["milk"]
    else:
        new_milk = _resources["milk"] - MENU[_choice]["ingredients"]["milk"]
    new_coffee = _resources["coffee"] - MENU[_choice]["ingredients"]["coffee"]

    new_resources = {
        "water": new_water,
        "milk": new_milk,
        "coffee": new_coffee,
    }
    return new_resources


def print_report(_resources, _cash):
    print(f"Water: {_resources['water']}ml \n"
          f"Milk: {_resources['milk']}ml \n"
          f"Coffee: {_resources['coffee']}ml \n"
          f"Money: ${_cash}")


def select_drink():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while user_choice != "espresso" \
            and user_choice != "latte" \
            and user_choice != "cappuccino" \
            and user_choice != "report" \
            and user_choice != "off":
        print(f"Your input: {user_choice}, is bad. Try again.")
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return user_choice


def check_resources(_choice, _resources):
    error_tracker = 0

    choice_water = MENU[_choice]["ingredients"]["water"]
    if _choice == "espresso":
        choice_milk = 0
    else:
        choice_milk = MENU[_choice]["ingredients"]["milk"]
    choice_coffee = MENU[_choice]["ingredients"]["coffee"]

    if choice_water > _resources["water"]:
        print("Sorry there is not enough water.")
        error_tracker += 1
    if choice_milk > _resources["milk"]:
        print("Sorry there is not enough milk.")
        error_tracker += 1
    if choice_coffee > _resources["coffee"]:
        print("Sorry there is not enough coffee.")
        error_tracker += 1
    return error_tracker
