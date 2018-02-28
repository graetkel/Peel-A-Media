
import nltk
from nltk.wsd import lesk

inappropriateWordList = {'shit', 'ass', 'fuck' }
inappropriateParsingList= {()}
kidFriendlyCount = 0;
var TEXT;

words = file(TEXT, “r”).read().split()
unqWords = sorted(set(word))
for word in unqWords:
	print words.count(word), word 

for w in words:
	