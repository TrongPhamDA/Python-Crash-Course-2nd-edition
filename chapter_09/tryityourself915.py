# 9-15. Lottery Analysis: You can use a loop to see how
# hard it might be to win the kind of lottery you just
# modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your
# ticket wins. Print a message reporting how many times
# the loop had to run to give you a winning ticket.

print("\nEx 9.15 Lottery Analysis\n" + "-"*70)

# Import choice() function from random library
from random import choice

# Make a class
class Lottery:
	"""docstring for Lottery"self, number=5"""
	def __init__(self, number=4):
		self.number = number
		self.letters = [1,2,3,4,5,6,7,8,9,0,"a","b","c","e","e"]
		self.winticket = ""
		self.choice = ""
	# make a method to return a new ticket
	def get_ticket(self):
		for i in range(self.number):
			self.choice = choice(self.letters)
			self.letters.remove(self.choice)
			self.winticket += str(self.choice).upper()
		return self.winticket

win_today = Lottery().get_ticket()
turns = 0

my_ticket = []
while True:
	current_ticket = Lottery().get_ticket()
	if current_ticket in my_ticket:
		continue
	my_ticket.append(current_ticket)
	turns += 1
	print(f"{turns:6d} - {current_ticket}")
	if current_ticket == win_today:
		break

print(f"\nWinning ticket is: {win_today}")
print(f"You win after    : {turns} tickets.")