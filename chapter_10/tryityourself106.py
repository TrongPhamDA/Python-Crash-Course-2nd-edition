# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to
# convert the input to an int, you’ll get a ValueError. Write a program
# that prompts for two numbers. Add them together and print the result.
# Catch the ValueError if either input value is not a number, and print
# a friendly error message. Test your program by entering two numbers
# and then by entering some text instead of a number.

print("\nEx 10.6 Addition\n" + "-"*70)
print("Give me a number\n")

try:
    num1 = input("First_number = ")
    num1 = int(num1)
except ValueError:
    print("Value Error!, Enter a number next time.")
else:
    print(f"Your number: {num1}")