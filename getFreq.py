import wsd_code as wc
import nltk

var TEXT;

words = file(TEXT, “r”).read().split()
unqWords = sorted(set(word))
for word in unqWords:
	print words.count(word), word 

for w in words:
	