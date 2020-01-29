import operator
import sys
sys.tracebacklimit = 0

class Strategy:
    comparison_operators = {"<": operator.lt, "<=": operator.le, "==": operator.eq, "!=": operator.ne, ">=": operator.ge, ">": operator.gt}
    def __init__(self, ruleJson):
        self.output = ""
        comparisonParameters = ruleJson["parameters"][0].split(".")
        self.compObj = comparisonParameters[0]
        self.compOperandL = comparisonParameters[1]
        self.compOperation = self.comparison_operators[ruleJson["operation"]]
        self.compOperandR = ruleJson["values"][0]
        mutationParameters = ruleJson["parameters"][1].split(".")
        self.mutObj = mutationParameters[0]
        self.mutOperandL = mutationParameters[1]
        self.mutOperandR = ruleJson["values"][1]
        self.inputVal = ruleJson["values"][1]
    def runStrategy(self, product, person):
        refObj = locals()[self.compObj]
        if self.compOperation(getattr(refObj, self.compOperandL), self.compOperandR):
            setattr(product, self.mutOperandL, self.resultOperation(getattr(product, self.mutOperandL), self.mutOperandR))
            self.updateOutput(product)

    
    def updateOutput(self, product):
        pass

class DecreaseRate(Strategy):
    def __init__(self, ruleJson):
        super().__init__(ruleJson)
        self.resultOperation = operator.isub
    
    def updateOutput(self, product):
        product.rate_changes += " - " + str(self.mutOperandR)

class IncreaseRate(Strategy):
    def __init__(self, ruleJson):
        super().__init__(ruleJson)
        self.resultOperation = operator.iadd

    def updateOutput(self, product):
        product.rate_changes += " + " + str(self.mutOperandR)

class Disqualified(Strategy):
    def __init__(self, ruleJson):
        super().__init__(ruleJson)
        self.resultOperation = operator.ior # works for our needs (assignment)

    def updateOutput(self, product):
        pass