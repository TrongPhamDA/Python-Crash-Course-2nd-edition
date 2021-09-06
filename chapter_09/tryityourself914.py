# 9-14. Lottery: Make a list or tuple containing a series
# of 10 numbers and five letters. Randomly select four
# numbers or letters from the list and print a message
# saying that any ticket matching these four numbers or
# letters wins a prize.

print("\nEx 9.14 Lottery\n" + "-"*70)

# Import choice() function from random library
from random import choice

# Make a class
class Lottery:
	"""docstring for Lottery"self, number=5"""
	def __init__(self, number=4):
		self.number = number
		self.letters = (1,2,3,4,5,6,7,8,9,0,"a","b","c","e","e")
		self.winticket = ""
	# make a method to return a winning ticket
	def get_win_ticket(self):
		for i in range(self.number):
			self.winticket += str(choice(self.letters)).upper()
		return self.winticket

win_today = Lottery()
print(f"Winning ticket is: {win_today.get_win_ticket()}")