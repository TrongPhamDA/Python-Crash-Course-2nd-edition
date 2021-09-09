# 10-12. Favorite Number Remembered

import json

filename = "favorite number.json"

def read_number():
    try:
        with open(filename, 'r') as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    while True:
        try:
            number = input("\nEnter your favorite number: ")
            number = int(number)
        except ValueError:
            print("Enter a number again, plz.")
            continue
        else:
            with open(filename, 'w') as f:
                json.dump(number, f)
                break
    return number

def show_number():
    number = read_number()
    if number:
        print(f"\nI know your favorite number! It’s {number}")
    else:
        number = get_new_number()
        print(f"\nWe 'll remember your favorite, {number}.")

show_number()