import nltk
import inspect
from nltk.wsd import lesk
from nltk.tag import pos_tag, map_tag
from nltk import corpus
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import PorterStemmer

ps = PorterStemmer()

inappropriateWordList = {'shit', 'ass', 'fuck', 'damn', 'dick', 'pussy', 'whore', 'cunt', 'crap'
, 'goddman', 'cum', 'piss', 'bitch', 'hell', 'cock', 'goddamn'}
kidFriendlyCount = 0
TEXT = open('../Peel-A-Media/JohnWickBabaYaga.txt', 'r')
words = TEXT.read()
sent_tokenize(words)
tokenWords = word_tokenize(words)
tokenWords = pos_tag(tokenWords)
for word in tokenWords:
    if word[0] is not None:
        temp = ps.stem(word[0])
    if temp in inappropriateWordList:
        if word[1] != "NNP":
            kidFriendlyCount += 1
print(tokenWords)
print(kidFriendlyCount)
