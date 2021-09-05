# 8-2. Favorite Book: Write a function called
# favorite_book() that accepts one parameter, title.
# The function should print a message, such as One
# of my favorite books is Alice in Wonderland.
# Call the function, making sure to include a book title
# as an argument in the function call.
print("\nEx 8.2 Favorite Book\n" + "-"*70)
def favorite_book(title):
	print(f"One of my favorite books is '{title.title()}'.")

favorite_book("thong ke ung dung - trong kinh te va kinh doanh")