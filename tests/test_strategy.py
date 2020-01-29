import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from strategy import *
import operator

def test_strategy_constructor():
    rules = {"action": "disqualify", "parameters": ["person.state", "product.disqualified"], "values": ["Florida", True], "operation": "=="}
    strat = Strategy(rules)
    assert strat.compOperation is operator.eq
    assert strat.compObj == "person"
    assert strat.compOperandL == "state"
    assert strat.compOperandR == "Florida"

def test_strategy_comp_equals():
    rules = {"action": "disqualify", "parameters": ["person.state", "product.disqualified"], "values": ["Florida", True], "operation": "=="}
    strat = Strategy(rules)
    assert strat.compOperation is operator.eq

def test_strategy_comp_gt():
    rules = {"action": "decrease_rate", "parameters": ["person.credit_score", "product.interest_rate"], "values": [740, 0.5], "operation": ">"}
    strat = Strategy(rules)
    assert strat.compOperation is operator.gt

def test_strategy_comp_ge():
    rules = {"action": "disqualify", "parameters": ["person.credit_score", "product.disqualified"], "values": [600, True], "operation": ">="}
    strat = Strategy(rules)
    assert strat.compOperation is operator.ge

def test_strategy_comp_lt():
    rules = {"action": "increase_rate", "parameters": ["person.credit_score", "product.interest_rate"], "values": [650, 1.5], "operation": "<"}
    strat = Strategy(rules)
    assert strat.compOperation is operator.lt

def test_strategy_comp_le():
    rules = {"action": "disqualify", "parameters": ["person.state", "product.disqualified"], "values": ["Florida", True], "operation": "<="}
    strat = Strategy(rules)
    assert strat.compOperation is operator.le