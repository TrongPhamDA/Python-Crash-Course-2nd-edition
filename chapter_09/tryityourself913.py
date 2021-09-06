# Import randit function from random library
from random import randint

# Make a class named Die
class Die:
	def __init__(self, sides=6):
		# default value of 6	
		self.sides = sides
	
	def describe_die(self):
		print(f"\nYour die has: {self.sides} sides")

	# Write a method called roll_die() that prints
	# a random number between 1 and self.sides
	def roll_die(self):
		return randint(1, self.sides)


die1 = Die()
die2 = Die(10)
die3 = Die(20)

die1.describe_die()
for i in range(10):
	# format :2d mean 2 digits
	print(f"- turn {i+1 :2d}: {die1.roll_die()}")

die2.describe_die()
for i in range(10):
	# format :2d mean 2 digits
	print(f"- turn {i+1 :2d}: {die2.roll_die()}")

die3.describe_die()
for i in range(10):
	# format :2d mean 2 digits
	print(f"- turn {i+1 :2d}: {die3.roll_die()}")