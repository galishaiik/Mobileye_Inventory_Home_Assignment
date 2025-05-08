class Product:
    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = amount

class Inventory:
    def __init__(self):
        self.products = {}

    def get_inventory_products_status(self):
        return self.products