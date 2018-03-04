import nltk
import inspect
from nltk.wsd import lesk
from nltk.tag import pos_tag, map_tag
from nltk import corpus
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer

inappropriateWordList = {'shit', 'ass', 'fuck', 'damn', 'dick', 'pussy'}
kidFriendlyCount = 0
TEXT = open('../Peel-A-Media/Buzzfeed.txt', 'r')
words = TEXT.read()
sent_tokenize(words)

tokenWords = word_tokenize(words)
tokenWords = pos_tag(tokenWords)
for word in tokenWords:
    print(word[0])
    if word[0] in inappropriateWordList:
        if word[1] != "NNP":
            kidFriendlyCount += 1
print(tokenWords)
print(kidFriendlyCount)
