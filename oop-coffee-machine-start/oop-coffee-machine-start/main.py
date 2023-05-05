from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


coffee_machine_is_on = True
while coffee_machine_is_on:
    choice = input(f"please type which you want {menu.get_items()}")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif choice == "close":
        coffee_machine_is_on = False
    elif choice in menu.get_items().split("/"):
        menu_item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
    else:
        print(f"Your input '{choice}' was not valid, please try again")
