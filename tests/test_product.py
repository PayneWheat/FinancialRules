import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from product import Product

def test_product():
    product = Product("7-1 ARM", 5.0)
    assert product.name == "7-1 ARM"
    assert product.interest_rate == 5.0