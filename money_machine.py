class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = \
            [
                { "name": "quarters", "value": 25 },
                { "name": "dimes", "value": 10 },
                { "name": "nickles", "value": 5 },
                { "name": "pennies", "value": 1 }
            ]

    def __init__( self ):
        self.profit = 0
        self.money_received = 0

    def dots( self, string, width ):
        return width - len(string)

    def report( self ):
        """
        Prints the current profit
        """
        print(f" Money {'.' * 29} {self.CURRENCY}{self.profit:1.2f}\n")

    def process_coins( self ):
        """
        Returns the total calculated from coins inserted.
        """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * \
                                   self.COIN_VALUES[coin]
        return self.money_received

    def make_payment( self, cost ):
        """
        Returns True when payment is accepted, or False if insufficient.
        """
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

    def collect_coins( self, selection, cost ):
        coins = \
            [
                { "name": "quarters", "value": 25 },
                { "name": "dimes", "value": 10 },
                { "name": "nickles", "value": 5 },
                { "name": "pennies", "value": 1 }
            ]
        print(f"A {selection} costs {self.CURRENCY}{cost:0.2f}\nPlease insert some coins.")

        coins_total = 0

        while True:
            for coin in range(len(coins)):
                received = int(
                    input(
                        f"${cost - coins_total:>5.2f}: How many {coins[coin]['name']}? "))

                coins_total += (coins[coin]['value'] / 100) * received

                if int(coins_total * 100) >= int(cost * 100):
                    change = coins_total - cost
                    if change:
                        print(f"Here is your {self.CURRENCY}{change:0.2f} change")
                        return
