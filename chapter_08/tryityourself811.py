# 8-11. Archived Messages: Start with your work from
# Exercise 8-10. Call the function send_messages() with
# a copy of the list of messages. After calling the
# function, print both of your lists to show that the
# original list has retained its messages.

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

# Make a copy of unprinted_lyric with slicer [:]
sent_message(unprinted_lyric[:], printed_lyric)

print("\nAfter:")
print(unprinted_lyric)
print(printed_lyric)