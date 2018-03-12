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
            hashmap[time] = line
            line = ""
        else:
            line = line + " " + words[i]
            i = i+1
    line = line + " " + words[i]
    hashmap[time] = line
    # can split the keywords and do loop minimizing.
    text = input("enter the time stamp you are looking for: ")
    subject.getSub(text)
    keyword = "world"
    count = 0

<<<<<<< HEAD
words = [''.join(c for c in s if c not in string.punctuation)for s in words]
length = len(words)
time = 0
line = ""
for i in range(length-1):
    if words[i].isdigit():
        time = i
    if words[i+1].isdigit() and (i+1) < length-1:
        line = line + " " + words[i]
        hashmap[time] = line
        line = ""
    else:
        line = line + " " + words[i]
        i = i+1
# can split the keywords and do loop minimizing.
keyword = "time"
count = 0;
for x in hashmap:
    split = hashmap[x].split()
    for s in split:
        if(s == keyword):
            print(hashmap[x])
            count = count + 1;
if(count == 0):
    print("'" + keyword + "' is never spoken in the video")
=======
    sentence = ""
    for x in hashmap:
        split = hashmap[x].split()
        for s in split:
            if(s == keyword):
                sentence = sentence + hashmap[x] + "\n"
                count = count + 1
    if(count == 0):
        sentence = "'" + keyword + "' is never spoken in the video"
    return sentence

def getLastTime(self):
    lastTime = (self.lastTime / 100) * 60
    return lastTime 
>>>>>>> origin/master
