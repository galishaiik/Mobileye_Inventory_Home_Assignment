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

def test_inventory_remove_product(filled_inventory):
    # Remove "Banana" product
    updated_products = filled_inventory.remove_product("Banana")
    # Verify "Banana" product removed
    assert "Banana" not in updated_products
    # Verify "Apple" product still in dict
    assert updated_products == {'Apple': 25, "pineapple": 37.2}

def test_get_existing_product(filled_inventory):
    name, amount = filled_inventory.get_product("pineapple")
    assert name == "pineapple"
    assert amount == 37.2

def test_get_nonexistent_product(filled_inventory):
    name, amount = filled_inventory.get_product("Juice")
    assert name == "Juice"
    assert amount == 0