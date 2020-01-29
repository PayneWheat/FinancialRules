from strategy import *
import sys
sys.tracebacklimit = 0

class Rule:
    strategy_constructors = {"decrease_rate": DecreaseRate, "increase_rate": IncreaseRate, "disqualify": Disqualified}
    def __init__(self, ruleJson):
        self.strategy = self.strategy_constructors[ruleJson["action"]](ruleJson)

    def runStrategy(self, product, person):
        self.strategy.runStrategy(product, person)
