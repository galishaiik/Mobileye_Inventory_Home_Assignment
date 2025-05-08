from Mobileye_Classes import Product

def test_inventory_add_product(empty_inventory):
    inventory = empty_inventory

    # Verify no items inside inventory dict
    assert inventory.get_inventory_products_status() == {}

    # Add a new product
    product1 = Product(name="Apple", amount=10)
    updated_status = inventory.add_product(product1)
    assert updated_status == {"Apple": 10}
    assert inventory.get_inventory_products_status() == {"Apple": 10}

    # Add more of the same product
    product2 = Product(name="Apple", amount=5)
    updated_status = inventory.add_product(product2)
    assert updated_status == {"Apple": 15}
    assert inventory.get_inventory_products_status() == {"Apple": 15}

    # Add a different product
    product3 = Product(name="Banana", amount=8)
    updated_status = inventory.add_product(product3)
    assert updated_status == {"Apple": 15, "Banana": 8}
    assert inventory.get_inventory_products_status() == {"Apple": 15, "Banana": 8}