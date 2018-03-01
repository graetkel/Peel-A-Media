
import nltk
from nltk.wsd import lesk

from nltk import corpus
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer
inappropriateWordList = {'shit', 'ass', 'fuck', 'damn', 'dick', 'pussy'}
kidFriendlyCount = 0
TEXT = open('../Peel-A-Media/Buzzfeed.txt', 'r')
words = TEXT.read().split()
#sent_tokenize(words)
#tokenWords = TreebankWordTokenizer().tokenize(words)
unqWords = sorted(set(words))
for word in unqWords:
	print(words.count(word), word) 

	
