import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from product import Product
from person import Person
from rulesengine import RulesEngine

def test_rulesengine():
    person = Person(720, "Florida")
    product = Product("7-1 ARM", 5.0)
    rules_engine = RulesEngine()
    #rules = rules_engine.loadRules("rules.json")
    rules = ""
    rules_engine.loadRules("rules.json")
    assert rules_engine.status == "Loading rules.json"
    rules_engine.runRules(person, product, rules)
    assert rules_engine.status == "Rules ran"

    