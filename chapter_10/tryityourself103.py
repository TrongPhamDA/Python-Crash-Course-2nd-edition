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
guest_name = input("Enter your name, plz: ")
with open(guest_file, "a") as guest_register:
	guest_register.write(guest_name + "\n")
print("Thank you!")