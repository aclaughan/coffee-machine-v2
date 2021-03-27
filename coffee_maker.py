from art import cup

class CoffeeMaker:
    """
    Models the machine that makes the coffee
    """

    def __init__( self ):
        self.resources = \
            {
                "water":
                    {
                        "amount": 300,
                        "unit": "ml"
                    },

                "milk":
                    {
                        "amount": 200,
                        "unit": "ml"
                    },

                "coffee":
                    {
                        "amount": 100,
                        "unit": "g"
                    }
            }

    def dots( self, string, width ):
        return width - len(string)


    def header( self, heading ):
        new_string = ''
        for character in heading.upper():
            new_string += character + ' '

        width = len(new_string) + 1
        print(f" {new_string}\n{'-' * width}")

        return len(new_string)

    def report( self ):
        """
        Prints a report of all resources.
        """
        header_width = self.header('coffee machine report') +4
        print(f" resources available:\n")

        for i in self.resources:
            message = f"  {i}  {self.resources[i]['amount']:0.2f}{self.resources[i]['unit']}"
            print(
                f" {i} " \
                f"{'.' * self.dots(message, header_width)} " \
                f"{self.resources[i]['amount']}" \
                f"{self.resources[i]['unit']} "
            )



    def is_resource_sufficient( self, drink ):
        """
        Returns True when order can be made,
        False if ingredients are insufficient.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]['amount']:
                print(f"Sorry there is not enough {item}.\n")
                can_make = False

        return can_make


    def make_coffee( self, order ):
        """
        Deducts the required ingredients from the resources.
        """
        print(f"creating a fresh {order.name} masterpiece.")
        for item in order.ingredients:
            self.resources[item]['amount'] -= order.ingredients[item]
        print(f"\n{cup}\nEnjoy your coffee and have a great day\n")
