class MenuItem:
    """
    Models each Menu Item.
    """

    def __init__( self, name, water, milk, coffee, cost ):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
    Models the Menu with drinks.
    """

    def __init__( self ):
        self.menu = [
            MenuItem(
                name = "espresso",
                water = 50,
                milk = 0,
                coffee = 18,
                cost = 1.5
            ),

            MenuItem(
                name = "latte",
                water = 200,
                milk = 150,
                coffee = 24,
                cost = 2.5
            ),
            MenuItem(
                name = "cappuccino",
                water = 250,
                milk = 50,
                coffee = 24,
                cost = 3
            ),
        ]

    def header( self, heading ):
        new_string = ''
        for character in heading.upper():
            new_string += character + ' '

        width = len(new_string) + 1
        print(f" {new_string}\n{'-' * width}")

        return len(new_string)

    def expand_selection( self, selection ):
        expanded = {
            'e': 'espresso',
            'l': 'latte',
            'c': 'cappuccino',
            'o': 'off',
            'r': 'report'
        }

        return expanded[selection]

    def get_items( self, drink ):
        """
        Returns all the names of the available menu items
        """
        options = ""
        for item in self.menu:
            if item.name == drink:
                return item

    def find_drink( self, order_name ):
        """
        Searches the menu for a particular drink by name.
        Returns that item if it exists, otherwise returns None
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

    def display( self ):
        """
        displays the various coffee options
        :return: (str) selection
        """
        selection = ''
        while selection not in ['e', 'l', 'c', 'o', 'r']:
            header_width = self.header('coffee machine menu')
            print(f" prices:\n")
            for i in self.menu:
                message = f"{i.name}{i.cost:0.2f}"
                print(f" {i.name} " \
                      f"{'.' * self.dots(message, header_width)} " \
                      f"${i.cost:0.2f}")
            selection = input( \
                "\nWhat would you like? (espresso/latte/cappuccino):\n  > "
            ).lower()[:1]

        return self.expand_selection(selection)

    def dots( self, string, width ):
        return width - len(string) - 4
