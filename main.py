from person import Person
from product import Product
from rulesengine import RulesEngine

person = Person(750, "Texas")
product = Product("Prod1", 5.0)
r = RulesEngine()
r.loadRules("rules.json")
r.runRules(person, product)

product = Product("7-1 ARM", 5.0)
r.runRules(person, product)

person = Person(700, "Florida")
product = Product("7-1 ARM", 5.0)
r.runRules(person, product)
