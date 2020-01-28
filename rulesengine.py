import json
from person import Person
from product import Product
from rule import Rule

class RulesEngine:
    # should be a singleton
    def __init__(self):
        self.rules = []
    def runRules(self, person, product):
        print("Running rules...")
        for rule in self.rules:
            rule.runStrategy(product, person)
        print("Product name:\t", product.name)
        print("Interest rate:\t", product.interest_rate)
        print("Disqualified:\t", product.disqualified)
        print("")
    def loadRules(self, location):
        print("Loading " + location)
        with open(location) as rules:
            data = json.load(rules)
            for rule in data:
                self.rules.append(Rule(rule))


