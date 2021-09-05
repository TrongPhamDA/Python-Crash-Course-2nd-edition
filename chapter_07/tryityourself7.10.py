# 7-10. Dream Vacation: Write a program that polls
# users about their dream vacation. Write a prompt
# similar to If you could visit one place in the world,
# where would you go? Include a block of code that
# prints the results of the poll.
print("\nEx 7.10 Drem Vacation\n" + "-"*70)
responses = {}
poll_active = True

while poll_active:
    name = input("\nYour name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    responses[name] = place

    repeat = ""
    while repeat not in ["y", "n", "Y", "N"]:
        repeat = input("Another respond (y/n)? ")
    if repeat in ["n", "N"]:
        poll_active = False
        
print("\nAll respond:")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
