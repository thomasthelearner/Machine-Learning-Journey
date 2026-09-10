class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    def get_price(self, coffee_type):
        if coffee_type in self.menu:
            return self.menu[coffee_type]
        else:
            raise ValueError(f"{coffee_type} is not available in the menu.")

    def add_item(self, coffee_type, price):
        if coffee_type in self.menu:
            raise ValueError(f"{coffee_type} already exists in the menu.")
        self.menu[coffee_type] = price