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
temp = False
index = 0
for word in words:
    if index > 0:
        if word == "[":
            temp = True
    if index < len(words) - 1:
        if word == "]":
            temp = False
            words = words.replace(word,"")
            index += 1
            words = words.replace(words[index], "")
    if temp:
        words = words.replace(word,"")
    index += 1
words = sent_tokenize(words)


print(words)
