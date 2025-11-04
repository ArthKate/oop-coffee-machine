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
    beverageNameAndCost = [(beverage.name, beverage.cost) for beverage in menu.menu]
    for name, cost in beverageNameAndCost:
        print(f"{name.capitalize():<15} ${cost:.2f}")
    return ""


print(print_menu())
print("-----------------------")

#Retrieves the drink from the menu
def retrieve_drink(beverage_name):
        order =  menu.find_drink(beverage_name)
        return order.name

order = retrieve_drink('latte')
print(order)

resource_status = coffee_maker.is_resource_sufficient(menu.find_drink('latte'))
print(resource_status)

#Receive payment
payment = money_machine.process_coins()
print(f"Payment received: ${payment}")

#validate payment transaction
# payment_status = money_machine.make_payment(menu.find_drink('latte').cost)






