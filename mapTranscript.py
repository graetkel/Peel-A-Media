from itertools import chain
from nltk.corpus import wordnet
import sys
import os
import string
import get_sub as subject
hashmap = {}
lastTime = 0

def getSentence(self, arg1):
    words = arg1.split()
    words = [''.join(c for c in s if c not in string.punctuation)for s in words]
    length = len(words)
    time = 0
    line = ""
    
    for i in range(length - 1):
        if (words[i].isdigit()):
            if (int(words[i]) > self.lastTime):
                self.lastTime = int(words[i])
        if (words[i].isdigit()):
            time = i
            
        if words[i+1].isdigit() and (i+1) < length-1:
            line = line + " " + words[i]
            hashmap[time] = line.lower()
            line = ""
        else:
            line = line + " " + words[i]
            i = i+1
    line = line + " " + words[i]
    hashmap[time] = line
    # can split the keywords and do loop minimizing.
    text = input("enter the time stamp you are looking for: ")
    arr = subject.getSub(text)
    synRoot = []
    synNSub = []
    synDObj = []
    synPObj = []
    synDSubPass = []
    synCom = []
    if (len("" + arr[0]) > 0):
        synonyms = wordnet.synsets(("" + arr[0]))
        synRoot = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    
    if (len("" + arr[1]) > 0):
        synonyms = wordnet.synsets(("" + arr[1]))
        synNSub = set(chain.from_iterable([word.lemma_names() for word in synonyms]))

    if (len("" + arr[2]) > 0):
        synonyms = wordnet.synsets(("" + arr[2]))
        synDObj = set(chain.from_iterable([word.lemma_names() for word in synonyms]))

    if (len("" + arr[3]) > 0):
        synonyms = wordnet.synsets(("" + arr[3]))
        synPObj = set(chain.from_iterable([word.lemma_names() for word in synonyms]))

    if (len("" + arr[4]) > 0):
        synonyms = wordnet.synsets(("" + arr[4]))
        synDSubPass = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    if (len("" + arr[5]) > 0):
        synonyms = wordnet.synsets(("" + arr[5]))
        synCom = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    rootSen = []
    nSubSen = []
    dObjSen = []
    pObjSen = []
    comSen = []
    result1 = []
    result = []
    nSubPassSen = []
    keyword = ("" + arr[0]).lower()
    count = 0
    sentence = ""
    for x in hashmap:
        split = hashmap[x].split()
        for s in split:
            for word in synRoot:
                if(s.lower() == word.lower()):
                    sentence = "" + hashmap[x] + "\n"
                    if (sentence not in rootSen):
                        rootSen.append(sentence)
            for word in synNSub:
                if(s.lower() == word.lower()):
                    sentence = "" + hashmap[x] + "\n"
                    if (sentence not in nSubSen):
                        nSubSen.append(sentence)
            for word in synDObj:
                if(s.lower() == word.lower()):
                    sentence = "" + hashmap[x] + "\n"
                if (sentence not in dObjSen):
                    dObjSen.append(sentence)
            for word in synPObj:
                if(s.lower() == word.lower()):
                    sentence = "" + hashmap[x] + "\n"
                    if (sentence not in pObjSen):
                        pObjSen.append(sentence)
            for word in synDSubPass:
                if(s.lower() == word.lower()):
                    sentence = "" + hashmap[x] + "\n"
                    if (sentence not in nSubPassSen):
                        nSubPassSen.append(sentence)
            for word in synCom:
                if(s.lower() == word.lower()):
                    sentence = "" + hashmap[x] + "\n"
                    if (sentence not in comSen):
                        comSen.append(sentence)
    for sen in rootSen:
        for sen1 in nSubSen:
            if (sen == sen1):
                if (sen not in result):
                    result.append(sen)  
        for sen1 in dObjSen:
            if (sen == sen1):
                if (sen not in result):
                    result.append(sen)      
        for sen1 in pObjSen:
            if (sen == sen1):
                if (sen not in result):
                    result.append(sen)  
        for sen1 in nSubPassSen:
            if (sen == sen1):
                if (sen not in result):
                    result.append(sen)  
        for sen1 in comSen:
            if (sen == sen1):
                if (sen not in result):
                    result.append(sen)  
    sentence = ""
    if(len(rootSen) == 0):
        sentence = "'" + arr[0] + "' is never spoken in the video"
    if (len(result) > 0):
        for sen in result:
            sentence = sentence + sen
    else:
        for sen in nSubSen:
            for sen1 in dObjSen:
                if (sen == sen1):
                    if (sen not in result):
                        result1.append(sen)      
            for sen1 in pObjSen:
                if (sen == sen1):
                    if (sen not in result):
                        result1.append(sen)  
            for sen1 in nSubPassSen:
                if (sen == sen1):
                    if (sen not in result):
                        result1.append(sen)  
            for sen1 in comSen:
                if (sen == sen1):
                    if (sen not in result):
                        result1.append(sen)  
        if (len(result1)):
            for sen in result1:
                sentence = sentence + sen
        else:
            for sen in rootSen:
                sentence = sentence + sen
    return sentence

def getLastTime(self):
    lastTime = (self.lastTime / 100) * 60
    return lastTime 
