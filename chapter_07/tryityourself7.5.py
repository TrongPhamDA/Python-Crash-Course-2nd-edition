# 7-5. Movie Tickets: A movie theater charges different
# ticket prices depending on a person’s age. If a person
# is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are
# over age 12, the ticket is $15. Write a loop in which
# you ask users their age, and then tell them the cost
# of their movie ticket.

print("\nEx 7.5" + "_"*50, end = "\n")
print("MOVIE TICKET")
while True:
	age = input("\nEnter 'quit' when you have done!\n"
		"How old are you?\n")
	if age == "quit":
		break
	age = int(age)
	if age < 3:
		ticket = 0
	elif age <= 12:
		ticket = 10
	else:
		ticket = 15
	if ticket == 0:
		answer = "free"
	else:
		answer = f"${ticket}"
	print(f"Your ticket is: {answer}")
print("Thank you!")