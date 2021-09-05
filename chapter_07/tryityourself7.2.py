# Ex 7-2. Restaurant Seating: Write a program that asks
# the user how many people are in their dinner group.
# If the answer is more than eight, print a message
# saying they’ll have to wait for a table. Otherwise,
# report that their table is ready
print("\nEx 7.2")
people_num = input("Hi, How many people are in your dinner group?\n")
people_num = int(people_num)
if people_num > 8:
	print("Oh sorry, you 'll have to wait for a table")
else:
	print("Thanks, your table is ready!")