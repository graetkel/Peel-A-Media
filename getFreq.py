
import nltk
from nltk.wsd import lesk

inappropriateWordList = {'shit', 'ass', 'fuck', 'damn', 'dick', 'pussy', 'cunt', 'fucking', 'fucked', 'crap', 'goddamn', 'holy shit', 'motherfucker', 'whore', 'twat', 'Shitbag', 'twat', 'Dickhead', 'Cumwipe', 'Piss', 'pissoff', 'bastard', 'Bitch', 'hell', 'cock'}
kidFriendlyCount = 0;
var TEXT;



words = file(TEXT, “r”).read().split()
unqWords = sorted(set(word))
for word in unqWords:
	print words.count(word), word

for w in words:
