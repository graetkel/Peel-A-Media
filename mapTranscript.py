import sys
import string
hashmap = {}

# TEXT = sys.argv[-1]
TEXT = "San Holo Transcript.txt"
words = open(TEXT, "r").read().split()
# print(words)

words = [''.join(c for c in s if c not in string.punctuation)for s in words]
length = len(words)
time = 0
line = ""
lastTime = 0
for i in range(length - 1):
    if (words[i].isdigit()):
        if (int(words[i]) > lastTime):
            lastTime = int(words[i])
    if (words[i].isdigit()):
        time = i
        print(time)
        
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
keyword = "world"
count = 0
def getLastTime( ):
    lastTime = (lastTime / 100) * 60
    return lastTime 

for x in hashmap:
    split = hashmap[x].split()
    for s in split:
        if(s == keyword):
            print(hashmap[x])
            count = count + 1
if(count == 0):
    print("'" + keyword + "' is never spoken in the video")
