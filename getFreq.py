
import nltk
from nltk.wsd import lesk
<<<<<<< HEAD

inappropriateWordList = {'shit', 'ass', 'fuck', 'damn', 'dick', 'pussy', 'cunt', 'fucking', 'fucked', 'crap', 'goddamn', 'holy shit', 'motherfucker', 'whore', 'twat', 'Shitbag', 'twat', 'Dickhead', 'Cumwipe', 'Piss', 'pissoff', 'bastard', 'Bitch', 'hell', 'cock'}
kidFriendlyCount = 0;
var TEXT;
=======
from nltk import corpus
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer
inappropriateWordList = {'shit', 'ass', 'fuck', 'damn', 'dick', 'pussy'}
kidFriendlyCount = 0
var TEXT
>>>>>>> origin/master



words = file(TEXT, “r”).read().split()
sent_tokenize(words)
tokenWords = TreebankWordTokenizer().tokenize(words)
unqWords = sorted(set(word))
for word in unqWords:
	print words.count(word), word

for w in words:
