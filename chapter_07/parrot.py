# # How the input() Function Works
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# # Letting the User Choose When to Quit
# prompt = "\nTell me something, and I will repeat it back to you:\nEnter 'quit' to end the program.\n"
# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit': print(message)

# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:\nEnter 'quit' to end the program.\n"
flag = True
while flag:
	message = input(prompt)
	if message == 'quit':
		flag = False
	else:
		print(message)