# 7-3. Multiples of Ten: Ask the user for a number,
# and then report whether the number is a multiple
# of 10 or not.
print("\nEx 7.3 Multiples of 10")
number = input("Pls enter a number: ")
number = int(number)
if number % 10 == 0:
	print(f"\n{number} is a multiple of 10")
else:
	print(f"\n{number} is not a multiple of 10")