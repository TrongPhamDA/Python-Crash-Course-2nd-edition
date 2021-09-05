# 8-8. User Albums: Start with your program from
# Exercise 8-7. Write a while loop that allows users
# to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s
# input and print the dictionary that’s created. Be
# sure to include a quit value in the while loop

print("\nEx 8.8 User Album\n" + "-"*70)
def make_album(title, artist = None, songs = None):
	title = title.title()
	album = {'album title' : title}
	if artist:
		album['artist'] = artist.title()
	else:
		album['artist'] = 'Linkin Park'
	if songs: album['number of songs'] = int(songs)
	return album
album_stored = {}
album_no = 0
album_name = ''
while True:
	print("\nEnter 'q' at any time to quit")
	input_artist = input("Enter album artist    : ")
	if input_artist in ['q', 'Q']: break
	input_title = input("Enter album title     : ")
	if input_title in ['q', 'Q']: break
	input_songs = input("Enter number of songs : ")
	if input_songs in ['q', 'Q']: break
	album_no += 1
	album_name = 'album ' + str(album_no)
	album_stored[album_name] = make_album(input_title, input_artist, input_songs)
if album_stored:
	print("-"*70 + "\nEntered albums:")
else:
	print("-"*70 + "\nThere aren't any stored albums")
for name, info in album_stored.items():
	print(f"{name}\n{info}\n")


