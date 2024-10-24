from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

# Classes used in the Coffee Machine Program
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

menu = Menu()

is_on = True

# Coffee Machine Interface

while is_on:
    options = menu.get_items()
    print("\nWelcome to Coffee Hut \n")
    choice = input(f"What would you like? ({options})\n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        report_type = input("Display which report? Supplies or Money? \n").title()
        if report_type == "Supplies":
            print(report_type)
            print("Please wait...")
            time.sleep(5)
            coffee_maker.report()
            input("Press Enter to continue...")
        elif report_type == "Money":
            print(report_type)
            print("Please wait...")
            time.sleep(5)
            money_machine.report()
            input("Press Enter to continue...")
        else:
            print(report_type)
            print("Invalid Input")
            input("Press Enter to continue...")
    else:
        print(f"{choice.title()}, nice choice!")
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost) == True:
            coffee_maker.make_coffee((drink))
        elif coffee_maker.is_resource_sufficient(drink) == False:
            print(f"I'm sorry, we are unable to make you {choice}")


