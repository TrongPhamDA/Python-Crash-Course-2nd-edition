import json

filename = "favorite number.json"

while True:
    try:
        number = input("Enter your favorite number: ")
        number = int(number)
    except ValueError:
        print("Enter a number again, plz.")
        continue
    else:
        with open(filename, 'w') as f:
            json.dump(number, f)
            break