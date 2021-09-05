# 7-4. Pizza Toppings: Write a loop that prompts the
# user to enter a series of pizza toppings until they
# enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to
# their pizza.

print("\nEx 7.4" + "_"*50, end = "\n")
print("Enter a topping you want to add to your pizza")
print("Enter 'done' if you don't want anything more.\n")
topping_selected = []
prompt = "Enter topping: "
enter_topping = ""
flag = True

while flag:
	enter_topping = input(prompt)
	if enter_topping == "done":
		flag = False
	else:
		topping_selected.append(enter_topping)
		print(f"I'll add {enter_topping.title()} to your pizza.\n")
print("\nThe toppings you have chosen:")
for topping in topping_selected:
	print(f"- {topping.title()}")
print("Thanks for your order.\n"
	"Your pizza will be served in less than 30 minutes!")
