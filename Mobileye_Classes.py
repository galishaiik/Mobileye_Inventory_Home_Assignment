class Product:
    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = amount

class Inventory:
    def __init__(self):
        self.products = {}

    def get_inventory_products_status(self):
        return self.products

    def add_product(self, product: Product):
        if product.name in self.products.keys():
            self.products[product.name] = self.products[product.name] + product.amount
        else:
            self.products[product.name] = product.amount
        return self.products

    def remove_product(self, product_name: str):
        if product_name in self.products.keys():
            del self.products[product_name]
            return self.products
        else:
            print(f'{product_name} not exists in inventory to delete')
            return self.products


inventory = Inventory()
inventory.add_product(Product("Apple", 5.0))
inventory.add_product(Product("Apple", 10.0))
inventory.add_product(Product("Banana", 15.0))
inventory.add_product(Product("pineapple", 45.0))