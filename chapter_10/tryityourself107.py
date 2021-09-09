# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in
# a while loop so the user can continue entering numbers even if
# they make a mistake and enter text instead of a number

print("\nEx 10.7 Addition Calculator\n" + "-"*70)
print("Give me a number\n")

while True:
    try:
        num1 = input("First_number = ")
        num1 = int(num1)
    except ValueError:
        print("Value Error!, Enter a number again\n")
        continue
    else:
        print(f"Your number: {num1}")
        break