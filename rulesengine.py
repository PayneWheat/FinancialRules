import json
from person import Person
from product import Product

class RulesEngine:
    # should be a singleton
    def __init__(self):
        self.rules = []
    def runRules(self, person, product):
        print("Running rules...")
        for rule in self.rules:
            print(type(rule.strategy))
            #if getattr(product, rule.prodAttr) == rule.prodVal:
            #    rule.runStrategy(product)
            rule.runStrategy(product, person)
        print(product.name)
        print(product.interest_rate)
        print(product.disqualified)
        print('')

    def loadRules(self, location):
        print("Loading " + location)
        self.status = "Loading " + location
        with open(location) as rules:
            data = json.load(rules)
            for p in data:
                self.rules.append(Rule(p))
        

class Rule:
    # composite
    def __init__(self, ruleJson):
        if ruleJson["action"] == "reduce_rate":
            self.strategy = DecreaseRate(ruleJson)
        elif ruleJson["action"] == "increase_rate":
            self.strategy = IncreaseRate(ruleJson)
        elif ruleJson["action"] == "disqualified":
            self.strategy = Disqualified(ruleJson)
    def runStrategy(self, product, person):
        self.strategy.runStrategy(product, person)

class Strategy:
    def __init__(self, ruleJson):
        parameter = ruleJson["parameters"][0].split(".")
        print("Parameter:")
        print(parameter)
        self.obj = parameter[0]
        self.attr = parameter[1]
        self.op = ruleJson["operations"][0]
        self.val = ruleJson["values"][0]
        print("Strategy init")
        print(ruleJson)
        self.ruleJson = ruleJson
    def runStrategy(self, product, person):
        pass
    

class DecreaseRate(Strategy):
    def __init__(self, ruleJson):
        super().__init__(ruleJson)
        print("DecreaseRate Strategy init: product.interest_rate -= " + str(ruleJson["values"][1]))
        #print(product.interest_rate + "-=" + value)
    def runStrategy(self, product, person):
        print("DecreaseRate Strategy called: " + str(self.ruleJson["parameters"][0]))
        if self.op == ">=" and self.obj == "person":
            print("Operation: greater than or equals to")
            if getattr(person, self.attr) >= self.ruleJson["values"][0]:
                print("Condition is met!")
                product.interest_rate -= self.ruleJson["values"][1]
            
        #if getattr(product, self.ruleJson["parameters"][0]) == self.ruleJson["values"][0]:
        #    product.interest_rate -= self.ruleJson["values"][1]

        
class IncreaseRate(Strategy):
    def __init__(self, ruleJson):
        super().__init__(ruleJson)
        print("IncreaseRate Strategy init: product.interest_rate += " + str(ruleJson["values"][1]))
    def runStrategy(self, product, person):
        print("IncreaseRate Strategy called")
        if self.op == "==" and self.obj == "product":
            if getattr(product, self.attr) == self.ruleJson["values"][0]:
                print("Condition is met!")
                product.interest_rate += self.ruleJson["values"][1]
        #product.interest_rate += self.ruleJson["values"][1]

class Disqualified(Strategy):
    def __init__(self, ruleJson):
        super().__init__(ruleJson)
        print("Disqualified Strategy init: product.disqualified = True")

    def runStrategy(self, product, person):
        if self.op == "==" and self.obj == "person":
            if getattr(person, self.attr) == self.ruleJson["values"][0]:
                print("Condition is met!")
                product.disqualified = True