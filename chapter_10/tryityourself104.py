# 10-3. Guest: Write a program that prompts the user for
# their name. When they respond, write their name to a
# file called guest.txt.

# 10-4. Guest Book: Write a while loop that prompts users
# for their name. When they enter their name, print a
# greeting to the screen and add a line recording their
# visit in a file called guest_book.txt. Make sure each
# entry appears on a new line in the file.

# 10-5. Programming Poll: Write a while loop that asks
# people why they like programming. Each time someone
# enters a reason, add their reason to a file that
# stores all the responses.

guest_file = "guest.txt"
guest_book = "guest_book.txt"

while True:
	guest_name = input("\nEnter 'q' at any time to quit.\nEnter your name, plz: ")
	guest_name = str(guest_name)
	if guest_name in ['q', 'Q']:
		break
	greet_message = f"Welcome you back, {guest_name.title()}"
	print(greet_message)

	with open(guest_file, "a") as guest_register:
		guest_register.write(guest_name + "\n")
	with open(guest_book, "a") as guest_greeting:
		guest_greeting.write(greet_message + "\n")