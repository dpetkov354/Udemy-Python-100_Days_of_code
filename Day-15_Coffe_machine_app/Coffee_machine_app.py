from Coffee_machine_app_assets import MENU
from Coffee_machine_app_assets import resources

machine_off = False
money = 0.0

while not machine_off:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == "off":
        machine_off = True
        break
    elif command == "report":
        print(f'Water: {resources["water"]}ml.')
        print(f'Milk: {resources["milk"]}ml.')
        print(f'Coffee: {resources["coffee"]}g.')
        print(f'Money: ${money:.2f}.')
    elif command == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        else:
            print("Sorry there is not enough water.")
            machine_off = True
            break
        if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        else:
            print("Sorry there is not enough coffee.")
            machine_off = True
            break
    elif command == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
        else:
            print("Sorry there is not enough water.")
            machine_off = True
            break
        if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        else:
            print("Sorry there is not enough coffee.")
            machine_off = True
            break
        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        else:
            print("Sorry there is not enough milk.")
            machine_off = True
            break
    elif command == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        else:
            print("Sorry there is not enough water.")
            machine_off = True
            break
        if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        else:
            print("Sorry there is not enough coffee.")
            machine_off = True
            break
        if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        else:
            print("Sorry there is not enough milk.")
            machine_off = True
            break

    print("Please insert you coins quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
    quarter_coins = int(input("How many quarters do you wish to insert: "))
    dimes_coins = int(input("How many dimes do you wish to insert: "))
    nickles_coins = int(input("How many nickles do you wish to insert: "))
    pennies_coins = int(input("How many pennies do you wish to insert: "))
    total_payment = (0.25 * quarter_coins) + (0.10 * dimes_coins) + (0.05 * nickles_coins) + (0.01 * pennies_coins)

    if command == "espresso":
        if total_payment >= MENU["espresso"]["cost"]:
            money += MENU["espresso"]["cost"]
            total_payment -= MENU["espresso"]["cost"]
            if total_payment > 0:
                print(f"Here is your change ${total_payment:.2f}.")
                print(f"Here is your ☕ espresso.Enjoy!")
            elif total_payment == 0:
                more_money = total_payment - MENU["espresso"]["cost"]
                print(f"Here is your ☕ espresso.Enjoy!")
        else:
            more_money = total_payment - MENU["espresso"]["cost"]
            print(f"Not enough money! You need ${(abs(more_money)):.2f}.")
    if command == "latte":
        if total_payment >= MENU["latte"]["cost"]:
            money += MENU["latte"]["cost"]
            total_payment -= MENU["latte"]["cost"]
            if total_payment > 0:
                print(f"Here is your change ${total_payment:.2f}.")
                print(f"Here is your ☕ latte.Enjoy!")
            elif total_payment == 0:
                more_money = total_payment - MENU["latte"]["cost"]
                print(f"Here is your ☕ latte.Enjoy!")
        else:
            more_money = total_payment - MENU["latte"]["cost"]
            print(f"Not enough money! You need ${(abs(more_money)):.2f}.")
    if command == "cappuccino":
        if total_payment >= MENU["cappuccino"]["cost"]:
            money += MENU["cappuccino"]["cost"]
            total_payment -= MENU["cappuccino"]["cost"]
            if total_payment > 0:
                print(f"Here is your change ${total_payment:.2f}.")
                print(f"Here is your ☕ cappuccino.Enjoy!")
            elif total_payment == 0:
                more_money = total_payment - MENU["cappuccino"]["cost"]
                print(f"Here is your ☕ cappuccino.Enjoy!")
        else:
            more_money = total_payment - MENU["cappuccino"]["cost"]
            print(f"Not enough money! You need ${(abs(more_money)):.2f}.")
