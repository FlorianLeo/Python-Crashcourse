def make_album(artist_name, album_title, song=None):
	album = {'artist': artist_name, 'title': album_title}
	if song:	
		album['song'] = song
	return album	
while True:
	print("\nPlease tell me yor favorite song:")
	artist = input("artist_name: ")
	if artist == 'q':
		break
	title = input("album_title: ")
	if title == 'q':
		break
	print(make_album(artist, title))