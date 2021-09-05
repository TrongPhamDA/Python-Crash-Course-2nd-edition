# 8-9. Messages: Make a list containing a series of short
# text messages. Pass the list to a function called
# show_messages(), which prints each text message.
print("\nEx 8.9 Messages\n" + "-"*70)
def show_messages(text_list):
	message_list = text_list[:]
	message_list.reverse()
	while message_list:
		current_message = message_list.pop()
		print(current_message)

hello_adele_lyric = ["Hello from the other side",
"I must've called a thousand times",
"To tell you I'm sorry for everything that I've done",
"But when I call, you never seem to be home"]

show_messages(hello_adele_lyric)