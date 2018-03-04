
import nltk
TEXT = open('../Peel-A-Media/Buzzfeed.txt', 'r')
words = TEXT.read().split()
unqWords = sorted(set(words))
for word in unqWords:
	print(words.count(word), word) 

	
