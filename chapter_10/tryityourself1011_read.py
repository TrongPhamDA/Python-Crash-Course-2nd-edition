import json

filename = "favorite number.json"

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print(f"Your favorite number hasn't been stored!")
else:
    print(f"I know your favorite number! It’s {number}")