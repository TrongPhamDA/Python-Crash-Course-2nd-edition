responses = {}

# Set a flag to indicate that polling is active.
active = True

while active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary.
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = ""
    while repeat not in ["yes", "no"]:
        repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat == 'no':
        active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
