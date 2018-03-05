import nltk
import inspect
import sys
from nltk.wsd import lesk
from nltk.tag import pos_tag, map_tag
from nltk import corpus
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import PorterStemmer


ps = PorterStemmer()

inappropriateWordList = {'shit', 'ass', 'asshole', 'asswipe', 'cuck', 'bullshit', 'fuck', 'damn', 'dick', 'pussy', 'whore', 'cunt', 'tawt', 'crap'
, 'goddman', 'cum', 'piss', 'bitch', 'slut', 'skank', 'motherfucker', 'hell', 'cock', 'goddamn', 'fuckers', 'fucked', 'fucking', 'fucker'}
kidFriendlyCount = 0
# TEXT = open('../Peel-A-Media/test.txt', 'r')
TEXT = open('../Peel-A-Media/tempTranscript.txt', 'r')
# TEXT = sys.argv[-1]
# TEXT = sys.argv[-1]
# words = TEXT.read()
words = TEXT.read()
sent_tokenize(words)
tokenWords = word_tokenize(words)
tokenWords = pos_tag(tokenWords)
for word in tokenWords:
    try:
        if word[0] is not None:
            temp = ps.stem(word[0])
        if temp in inappropriateWordList:
            if word[1] != "NNP":
                kidFriendlyCount += 1
    except:
        print(" ")
print(tokenWords)
print(kidFriendlyCount)
