def make_album(artist, album, numberofsongs=None):
	"""Returns a Dictionary with the Arguments passed to the function"""
	"""Required in order is: artist, album"""
	"""And OPTIONAL on the 3rd positon the numberofsongs"""
	dictionary_from_parameters = {'artist_name':artist, 'album_name':album}
	if numberofsongs:
		dictionary_from_parameters['songsOnAlbum'] = numberofsongs
	return dictionary_from_parameters

print(make_album('yello', 'trick'))
print(make_album('jean michelle jarree', 'equinox', 9))
print(make_album('van gelis', 'summer'))