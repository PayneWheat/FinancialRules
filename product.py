class Product:
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate
        self.disqualified = False
        self.rate_changes = str(self.interest_rate)