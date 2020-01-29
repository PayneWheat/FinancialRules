import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
import json
from rule import Rule
from strategy import *
from person import Person
from product import Product


def test_rule_constructor():
    s = {"action": "disqualify", "parameters": ["person.state", "product.disqualified"], "values": ["Florida", True], "operation": "=="}
    r = Rule(s)
    assert r is not None
    assert r.strategy is not None

def test_rule_disqualified():
    s = {"action": "disqualify", "parameters": ["person.state", "product.disqualified"], "values": ["Florida", True], "operation": "=="}
    r = Rule(s)
    assert r is not None
    assert type(r.strategy) is Disqualified

def test_rule_decrease_rate():
    s = {"action": "decrease_rate", "parameters": ["person.credit_score", "product.interest_rate"], "values": [720, 0.3], "operation": ">="}
    r = Rule(s)
    assert r is not None
    assert type(r.strategy) is DecreaseRate

def test_rule_increase_rate():
    s = {"action": "increase_rate", "parameters": ["product.name", "product.interest_rate"], "values": ["7-1 ARM", 0.5], "operation": "=="}
    r = Rule(s)
    assert r is not None
    assert type(r.strategy) is IncreaseRate

def test_rule_undefined_action():
    #with pytest.raises(KeyError):
    with pytest.raises(KeyError):
        s = {"action": "some_action", "parameters": ["product.name", "product.interest_rate"], "values": ["7-1 ARM", 0.5], "operation": "=="}
        person = Person(720, "Texas")
        product = Product("SomeProd", 5.0)
        r = Rule(s)
        r.runStrategy(product, person)

def test_rule_undefined_comp_operand():
    with pytest.raises(KeyError):
        s = {"action": "decrease_rate", "parameters": ["something.credit_score", "product.interest_rate"], "values": [720, 0.3], "operation": ">="}
        r = Rule(s)
        person = Person(720, "Texas")
        product = Product("SomeProd", 5.0)
        r.runStrategy(product, person)

def test_rule_undefined_product_attribute():
    with pytest.raises(AttributeError):
        s = {"action": "decrease_rate", "parameters": ["person.credit_score", "product.something"], "values": [720, 0.3], "operation": ">="}
        r = Rule(s)
        person = Person(720, "Texas")
        product = Product("SomeProd", 5.0)
        r.runStrategy(product, person)