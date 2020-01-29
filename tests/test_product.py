import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from product import Product

def test_product():
    product = Product("Example", 5.0)
    assert product.name == "Example"
    assert product.interest_rate == 5.0
    assert product.disqualified == False
    assert product.rate_changes == "5.0"