# 7-9. No Pastrami: Using the list sandwich_orders
# from Exercise 7-8, make sure the sandwich 'pastrami'
# appears in the list at least three times. Add code
# near the beginning of your program to print a message
# saying the deli has run out of pastrami, and then use
# a while loop to remove all occurrences of 'pastrami'
# from sandwich_orders. Make sure no pastrami sandwiches
# end up in finished_sandwiches.
print("\nEx 7.9 No Pastrami\n" + "-"*70)
sandwich_orders = ['pastrami', 'deli', 'roast beef', 'ham', 'pastrami', 'egg', 'chicken salad', 'pastrami']
finished_sandwiches = []

print("Your orders:")
for sandwich in sandwich_orders:
	print(f"\t- {sandwich.title()} sandwich")

print("\nSorry, the Deli has run out of pastrami sandwich.")
finished_sandwiches = sandwich_orders
while 'pastrami' in finished_sandwiches:
	finished_sandwiches.remove('pastrami')

print("\nCurrently, your orders:")
for sandwich in finished_sandwiches:
	print(f"\t- {sandwich.title()} sandwich")