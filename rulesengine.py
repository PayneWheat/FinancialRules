import json
from person import Person
from product import Product
from rule import Rule
import sys
sys.tracebacklimit = 0

class RulesEngine:
    def __init__(self):
        self.rules = []
    def runRules(self, person, product):
        for rule in self.rules:
            rule.runStrategy(product, person)
        print("product.interest_rate == " + str(product.interest_rate) + " (" + product.rate_changes + ")")
        print("product.disqualified == " + str(product.disqualified))
        print("")
    def loadRules(self, location):
        with open(location) as rules:
            data = json.load(rules)
            for rule in data:
                self.rules.append(Rule(rule))


