from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from pyfiglet import Figlet

#program start
font = Figlet(font='slant')
print(font.renderText('Coffee Machine'))

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

#print general report of the resources plus the profit
def report():
    coffee_maker.report()
    money_machine.report()

report()
print("")

# Retrieve the name of the drinks
retrieved_drink_name = menu.get_items()
#print(retrieved_drink_name)

#print Menu
def print_menu():
    s = "MENU"
    print(s.center(24, '-'))
    print("")
    beverage_and_cost = [(beverage.name, beverage.cost) for beverage in menu.menu]
    for name, cost in beverage_and_cost:
        print(f"{name.capitalize():<15} ${cost:.2f}")



print_menu()

print("-----------------------")


#process order
def process_order(drink_name):
    # 1. Find the drink
    drink = menu.find_drink(drink_name)
    if drink is None:
        return False

    # 2. Check resources FIRST
    if not coffee_maker.is_resource_sufficient(drink):
        return False

    # 3. Take payment (uses drink.cost)
    if not money_machine.make_payment(drink.cost):
        return False

    # 4. Make coffee
    coffee_maker.make_coffee(drink)
    return True


while is_on:
    while is_on:
        choice = input(f"\nPlease select operation (off, report) or order a drink ({menu.get_items()}): ").lower()
        if choice == "off":
            is_on = False
            print("Turning off coffee machine...")
        elif choice == "report":
            report()
        else:
            process_order(choice)






