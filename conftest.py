import pytest
from Mobileye_Classes import Inventory

@pytest.fixture
def empty_inventory():
    return Inventory()