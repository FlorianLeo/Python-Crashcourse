def inhalt_anzeigen(filename):
	try:
		with open(filename) as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, but the {filename} file was not found on this system.")
	else:
		each_line = contents.split()
		for element in each_line:
			print(element)
		print(f"End of file {filename}\n")

filelist = ['cats.txt', 'dogs.txt', 'birds.txt']
for element in filelist:
	inhalt_anzeigen(element)