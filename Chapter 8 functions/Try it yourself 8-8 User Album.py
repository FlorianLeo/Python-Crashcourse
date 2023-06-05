def make_album(artist, album, numberofsongs=None):
	"""Returns a Dictionary with the Arguments passed to the function"""
	"""Required in order is: artist, album"""
	"""And OPTIONAL on the 3rd positon the numberofsongs"""
	dictionary_from_parameters = {'artist_name':artist, 'album_name':album}
	if numberofsongs:
		dictionary_from_parameters['songsOnAlbum'] = numberofsongs
	return dictionary_from_parameters

while True:
	print("\nPlease enter an Artist and Album:")
	print("You may abort any time by entering 'q'")
	ask_user_artist = input("Artist´s Name: ")
	if ask_user_artist == 'q':
		break
	ask_user_album = input("Album´s Name: ")
	if ask_user_album == 'q':
		break
	dictionary_from_answers = {'artist':ask_user_artist, 'album':ask_user_album}
	print(dictionary_from_answers)