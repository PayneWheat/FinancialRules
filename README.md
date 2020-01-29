# Financial Rules Engine

## Installation
Ensure Python and pip are installed. Navigate to the directory you've cloned the project into and run:
```
pip install -r requirements.txt
```

## Tests
From the root directory, run the command
```
pytest tests
```

## rules.json
To define a new rule, select an action from `increase_rate`, `decrease_rate`, `disqualify`, select two parameters (the first is the parameter to use in the condition, the second is the product attribute that is to be altered), two values (the conditional value, and the value to change the attribute to/by), and the comparison operation.
```
{
    "action": "disqualify",
    "parameters": ["person.state", "product.disqualified"],
    "values": ["Florida", true],
    "operation": "=="
}
```
In the example above, product.disqualifed is set to true if person.state == "Florida".

```
{
    "action": "decrease_rate",
    "parameters": ["person.credit_score", "product.interest_rate"],
    "values": [720, 0.3],
    "operation": ">="
}
```
In this example, product.interest_rate is reduced by 0.3 if person.credit_score >= 720

One may want to add a rule that disqualifies any person that has a credit score below 600.
```
{
    "action": "disqualify",
    "parameters": ["person.credit_score", "product.disqualified"],
    "values": [600, true],
    "operation": "<"
}
```