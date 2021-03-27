import logging

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

logging.basicConfig(level = logging.DEBUG)


def main():
    is_on = True
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while is_on:
        selection = menu.display()
        ##print(coffee_maker.is_resource_sufficient('cappuccino'))

        if selection == 'off':
            print("Turning OFF the machine")
            is_on = False

        elif selection == 'report':
            coffee_maker.report()
            money_machine.report()

        else:
            options = menu.get_items(selection)
            if coffee_maker.is_resource_sufficient(options):
                money_machine.collect_coins(selection, options.cost)
                coffee_maker.make_coffee(options)


if __name__ == '__main__':
    main()

# logging.debug(stuff)
