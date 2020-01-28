import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
import json
from rule import Rule
from strategy import *
from person import Person
from product import Product


def test_rule_constructor():
    s = {"action": "disqualify", "parameters": ["person.state", "product.disqualified"], "values": ["Florida", True], "operations": ["==", "="]}
    r = Rule(s)
    assert r is not None
    assert r.strategy is not None

def test_rule_disqualified():
    s = {"action": "disqualify", "parameters": ["person.state", "product.disqualified"], "values": ["Florida", True], "operations": ["==", "="]}
    r = Rule(s)
    assert r is not None
    assert type(r.strategy) is Disqualified

def test_rule_decrease_rate():
    s = {"action": "decrease_rate", "parameters": ["person.credit_score", "product.interest_rate"], "values": [720, 0.3], "operations": [">=", "-="]}
    r = Rule(s)
    assert r is not None
    assert type(r.strategy) is DecreaseRate

def test_rule_increase_rate():
    s = {"action": "increase_rate", "parameters": ["product.name", "product.interest_rate"], "values": ["7-1 ARM", 0.5], "operations": ["==", "+="]}
    r = Rule(s)
    assert r is not None
    assert type(r.strategy) is IncreaseRate