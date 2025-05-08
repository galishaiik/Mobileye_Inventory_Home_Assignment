import pytest
from Mobileye_Classes import Inventory

@pytest.fixture
def empty_inventory():
    return Inventory()

@pytest.fixture
def filled_inventory():
    inventory = Inventory()
    inventory.products = {
        "Banana": 15,
        "Apple": 25,
        "pineapple": 37.2
    }
    return inventory