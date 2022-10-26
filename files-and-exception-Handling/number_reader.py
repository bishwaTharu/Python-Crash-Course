import json

with open('numbers.json') as f:
    numbers = json.load(f)

for num in numbers:
    print(num)