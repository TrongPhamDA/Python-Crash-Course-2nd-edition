# 8-10. Sending Messages: Start with a copy of your program
# from Exercise 8-9. Write a function called send_messages()
# that prints each text message and moves each message to
# a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make
# sure the messages were moved correctly.

print("\nEx 8.10 Messages\n" + "-"*70)
def sent_message(unprint, printed):
	unprint.reverse()
	while unprint:
		current_message = unprint.pop()
		printed.append(current_message)

unprinted_lyric = ["Hello from the other side",
"I must've called a thousand times",
"To tell you I'm sorry for everything that I've done",
"But when I call, you never seem to be home"]
printed_lyric = []

print("Before:")
print(unprinted_lyric)
print(printed_lyric)

sent_message(unprinted_lyric, printed_lyric)

print("\nAfter:")
print(unprinted_lyric)
print(printed_lyric)