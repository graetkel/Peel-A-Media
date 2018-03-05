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
index = 0
temp = ""
words = sent_tokenize(words)
        
#words = "".join(words)


#print(words)
