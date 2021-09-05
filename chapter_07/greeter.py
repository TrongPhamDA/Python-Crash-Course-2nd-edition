# # Writing Clear Prompts

# name = input("Please enter your name: ")
# print(f"\nHello, {name.title()}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?\n"

name = input(prompt)
print(f"\nHello, {name}!")