# 8-7. Album: Write a function called make_album() that
# builds a dictionary describing a music album. The
# function should take in an artist name and an album
# title, and it should return a dictionary containing
# these two pieces of information. Use the function
# to make three dictionaries representing different
# albums. Print each return value to show that the
# dictionaries are storing the album information correctly.

# Use None to add an optional parameter
# to make_album() that allows you to store the number
# of songs on an album. If the calling line includes
# a value for the number of songs, add that value to
# the album’s dictionary. Make at least one new function
# call that includes the number of songs on an album.

print("\nEx 8.7 Album\n" + "-"*70)
def make_album(title, artist = 'linkin park', songs = None):
	title = title.title()
	artist = artist.title()
	album = {'artist name' : artist,
	'album title' : title}
	if songs: album['number of songs'] = songs
	return album

new_album = make_album(artist = 'linkin park', title = 'hybrid theory')
print(new_album)

new_album = make_album('meteora','linkin park', 5)
print(new_album)

new_album = make_album(title='a thousand suns', songs = 15)
print(new_album)