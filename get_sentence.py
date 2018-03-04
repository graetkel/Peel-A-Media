import nltk
import inspect
from nltk.wsd import lesk
from nltk.tag import pos_tag, map_tag
from nltk import corpus
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import PorterStemmer


TEXT = open('../Peel-A-Media/JohnWickBabaYaga.txt', 'r')
words = TEXT.read()
words = sent_tokenize(words)
for word in words:
    print(word)
    if word[0] == "[" and word[len(word) - 1]:
        print(word)
        words.replace(word, "")
        


#print(words)
#tokenWords = word_tokenize(words)
#print(tokenWords)