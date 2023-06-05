def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry but the {filename} file was not found.")
	else:
		words_only_list = contents.split()
		number_of_words = len(words_only_list)
		print(f"The file {filename} contains approximately {number_of_words} words.")

#filename = 'allice.txt'
filename = 'alice.txt'
count_words(filename)