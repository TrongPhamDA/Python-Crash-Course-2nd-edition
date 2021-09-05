# 7-8. Deli: Make a list called sandwich_orders and
# fill it with the names of various sandwiches.
# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print
# a message for each order, such as I made your tuna
# sandwich. As each sandwich is made, move it to the
# list of finished sandwiches. After all the sandwiches
# have been made, print amessage listing each sandwich
# that was made.
print("\nEx 7.8 Deli\n" + "-"*70)
sandwich_orders = ['deli', 'roast beef', 'ham', 'egg', 'chicken salad']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	finished_sandwiches.append(sandwich)
	print(f"I made your {sandwich.title()} sandwich")
print("-"*70, end="\n")