
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_balance}")


def check_resources(ingredients, required_resources):
    for resource, quantity in required_resources.items():
        if quantity > ingredients[resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    return True


def make_coffee(ingredients, required_resources):
    for resource, quantity in required_resources.items():
        ingredients[resource] -= quantity


def ask_for_money(funds_received):
    print("Please insert coins.")
    quarters_received = float(input("how many quarters?"))
    dimes_received = float(input("how many dimes?"))
    nickels_received = float(input("how many nickels?"))
    pennies_received = float(input("how many pennies?"))

    funds_received += 0.25 * quarters_received + 0.1 * dimes_received + 0.05 * nickels_received + 0.01 * pennies_received

    return funds_received


def check_money(total_funds, selection_cost):
    if total_funds > selection_cost:
        change = float(total_funds - selection_cost)
        print(f"Here is ${change} dollars in change.")
        total_funds = selection_cost
        return total_funds
    else:
        print("Sorry that's not enough money. Money refunded.")
        return


total_balance = float(0)
funds_collected = float(0)

machine_off = False

while not machine_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == 'off':
        machine_off = True
    elif user_choice == 'report':
        print_report()
    elif user_choice in MENU:
        if check_resources(resources, MENU[user_choice]['ingredients']):
            funds_collected = ask_for_money(funds_collected)
            total_balance += check_money(funds_collected, MENU[user_choice]['cost'])
            funds_collected = 0
            make_coffee(resources, MENU[user_choice]['ingredients'])
            print(f"Here is your {user_choice}. Enjoy!")
    else:
        machine_off = True
        print("Goodbye.")
