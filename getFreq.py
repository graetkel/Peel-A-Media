import wsd_code as wc

var TEXT;

words = file(TEXT, “r”).read().split()
unqWords = sorted(set(word))
for word in unqWords:
	print words.count(word), word 
