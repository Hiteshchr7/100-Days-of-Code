from coffee_maker import CoffeeMaker
from menu import Menu,MenuItem
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


choice = input(f"What would you like? ({menu.get_items()}): ")

while choice != "off" :

    if choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else :
        drink = menu.find_drink(choice)
        if drink :
            if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
        


    choice = input(f"What would you like? ({menu.get_items()}): ")
