from data import resources
from data import MENU
from data import money


def report():
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"money: ${money:.2f}")


def enough_resources(order):
    ingredients = ["water", "milk", "coffee"]
    ingredients_needed = list(MENU[f"{order}"]["ingredients"].values())
    resource_list = list(resources.values())
    for i in range(3):
        if ingredients_needed[i] > resource_list[i]:
            print(f"sorry there is not enough {ingredients[i]}")
            return False
    return True


def check_money(order):
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    money_total = quarters + dimes + nickles + pennies
    if MENU[order]["cost"] > money_total:
        print(f"you don't have enough money we will refund you ${money_total:.2f}")
        return False
    elif MENU[order]["cost"] == money_total:
        money_total -= MENU[order]["cost"]
        print("you have no change")
        print(f"Here is your {MENU[order]} ☕️. Enjoy!")
        return True
    elif MENU[order]["cost"] < money_total:
        money_total -= MENU[order]["cost"]
        print(f"you have enough money we will give you ${money_total:.2f}")
        print(f"Here is your {order} ☕️. Enjoy!")
        return True


def reduce_resources(order):
    global money
    if order == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    elif order == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    elif order == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["milk"] -= MENU["espresso"]["ingredients"]["coffee"]
    money += MENU[order]["cost"]


def coffee_machine():
    coffee_machine_is_on = True
    while coffee_machine_is_on:
        order = input("please enter one of the following espresso/latte/cappuccino: ")
        if order == "report":
            report()
            coffee_machine()
        elif order == "close":
            exit()
        if not enough_resources(order):
            coffee_machine()
        if not check_money(order):
            coffee_machine()
        reduce_resources(order)


coffee_machine()
