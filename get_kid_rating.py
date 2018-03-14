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
badWordList = []
def getRating( arg1 , arg2):
    kidFriendlyCount = 0
    kidRating = 0
    words = arg1
    sent_tokenize(words)
    tokenWords = word_tokenize(words)
    tokenWords = pos_tag(tokenWords)
    for word in tokenWords:
        try:
            if word[0] is not None:
                temp = ps.stem(word[0])
            if temp in inappropriateWordList:
                if word[1] != "NNP":
                    badWordList.append("" + word[0].lower())
                    kidFriendlyCount += 1
        except:
            print("")
    count = arg2 / 60
    while (count > 0):
        kidFriendlyCount = kidFriendlyCount - 1
        count = count - 10

    if (kidFriendlyCount > 10):
        kidRating = 10
    elif (kidFriendlyCount < 0):
        kidRating = 0
    else:
        kidRating = kidFriendlyCount

    return kidRating

def getBadWords():
    return badWordList