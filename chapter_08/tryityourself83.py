# 8-3. T-Shirt: Write a function called make_shirt()
# that accepts a size and the text of a message that
# should be printed on the shirt. The function should
# print a sentence summarizing the size of the shirt
# and the message printed on it. Call the function
# once using positional argument

print("\nEx 8.3 T-Shirt\n" + "-"*70)

def make_shirt(size, text):
	print(f"\nYour T-Shirt:\n\t- size    : {size.title()}\n\t- message : {text}")

make_shirt('l','hello world!')
make_shirt(text="Hello world!", size="s")