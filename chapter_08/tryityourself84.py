# 8-4. Large Shirts: Modify the make_shirt() function so
# that shirts are large by default with a message that
# reads I love Python. Make a large shirt and a medium
# shirt with the default message, and a shirt of any
# size with a different message

print("\nEx 8.4 Large Shirt\n" + "-"*70)

def make_shirt(size = 'large', text = 'I love Python'):
	print(f"\nYour T-Shirt:\n\t- size    : {size.title()}\n\t- message : {text}")

# Make a large size and a medium size
make_shirt()
make_shirt('medium')

# Another shirt with different message
make_shirt(text='Python Crash Course')