import wsd_code as wc

var TEXT;

word = file(TEXT, “r”).read().split()
unqWords = sorted(set(word))
for word in unqWords:
	print word.count(word), word 