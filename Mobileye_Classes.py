class Product:
    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = amount

class Inventory:
    def __init__(self):
        self.products = {}