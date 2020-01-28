import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from product import Product
from person import Person
from rulesengine import RulesEngine

def test_rulesengine_normal():
    person = Person(700, "Texas")
    product = Product("Example", 5.0)
    rules_engine = RulesEngine()
    rules_engine.loadRules("rules.json")
    rules_engine.runRules(person, product)
    assert product.disqualified == False
    assert product.interest_rate == 5.0

def test_rulesengine_reduced():
    person = Person(740, "California")
    product = Product("Example", 5.0)
    rules_engine = RulesEngine()
    rules_engine.loadRules("rules.json")
    rules_engine.runRules(person, product)
    assert product.disqualified == False
    assert product.interest_rate == 4.7

def test_rulesengine_71ARM():
    person = Person(740, "California")
    product = Product("7-1 ARM", 5.0)
    rules_engine = RulesEngine()
    rules_engine.loadRules("rules.json")
    rules_engine.runRules(person, product)
    assert product.disqualified == False
    assert product.interest_rate == 5.2

def test_rulesengine_combined():
    person = Person(720, "Florida")
    product = Product("7-1 ARM", 5.0)
    rules_engine = RulesEngine()
    #rules = rules_engine.loadRules("rules.json")
    rules_engine.loadRules("rules.json")
    rules_engine.runRules(person, product)
    assert product.disqualified == True
    assert product.interest_rate == 5.2



    