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
        self.money_received = 0

    def dots( self, string, width ):
        return width - len(string)

    def report( self ):
        """
        Prints the current profit
        """
        print(f" Money {'.' * 29} {self.CURRENCY}{self.money_received:1.2f}\n")

    def collect_coins( self, selection, cost ):
        coins = \
            [
                { "name": "quarters", "value": 25 },
                { "name": "dimes", "value": 10 },
                { "name": "nickles", "value": 5 },
                { "name": "pennies", "value": 1 }
            ]
        print(
            f"A {selection} costs {self.CURRENCY}{cost:0.2f}\nPlease insert some coins.")

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
                        print(
                            f"Here is your {self.CURRENCY}{change:0.2f} change")
                        self.money_received += cost
                        return
