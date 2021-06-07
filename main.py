from functions import coins_summed, make_drink, print_report, select_drink, check_resources
from data import MENU, resources

CASH = 0
RESOURCES = resources


# MAIN
machine_on = True
while machine_on:
    user_choice = select_drink()
    if user_choice == "off":
        machine_on = False
        break
    elif user_choice == "report":
        print_report(RESOURCES, CASH)
    else:
        check = check_resources(user_choice, RESOURCES)
        if check == 0:
            print("Please insert coins.")
            ask_quarters = int(input("how many quarters?: "))
            ask_dimes = int(input("how many dimes?: "))
            ask_nickles = int(input("how many nickles?: "))
            ask_pennies = int(input("how many pennies?: "))
            cash_entered = coins_summed(ask_pennies, ask_nickles, ask_dimes, ask_quarters)
            calc_change = cash_entered - MENU[user_choice]["cost"]
            if calc_change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if calc_change > 0:
                    print(f"Here is ${calc_change} in change.")
                CASH += MENU[user_choice]["cost"]
                RESOURCES = make_drink(user_choice, RESOURCES)
                print(f"Here is your {user_choice}, enjoy!")
