from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
import string
import sys

# Word Sense Disambiguation
TEXT = raw_input("enter a file name: ")

words = file(TEXT, "r").read().split()
unqWords = sorted(set(words))
# removing punctuation
unqWords = [''.join(c for c in s if c not in string.punctuation)for s in unqWords]
# removing numbers (time)
unqWords = [''.join(c for c in s if not c.isdigit())for s in unqWords]

# removing empty string
unqWords = [s for s in unqWords if s]
print(unqWords)

#finding the synsets
for loop in unqWords:
    sys.stdout.write(loop + ": ")
    sys.stdout.flush()
    #still don't know how to get rid of the none
    print (lesk(unqWords, loop))
