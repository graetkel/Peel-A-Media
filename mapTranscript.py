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
for i in xrange(length-1):
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