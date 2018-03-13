
import re
hashmap = {}
lastTime = 0


path = '../Peel-A-Media/' + "tempTranscript.txt"
TEXT = open(path, 'r').read()


words = TEXT.split()
length = len(words)
time = 0
line = ""

for i in range(length - 1):

    temp = "" + words[i]
    if "$~$" in words[i]:
        # print(words[i])
        words[i] = words[i].rstrip('$~$')
        words[i] = words[i].lstrip('$~$')
        wordS = words[i].split(".")
        tempNum = int(wordS[0])
        # print (tempNum)
        tempMin = tempNum/60
        tempSec = tempNum%60
        colinR = "" #seconds
        colinL = "" + str(tempMin)
        if (tempSec < 10):
            colinR = "0" + str(tempSec)
        else:
            colinR = "" + str(tempSec)

        tempTime = colinL + ':' + colinR

        words[i] = tempTime + '$~$'



fh = open("tempTranscript.txt","w")


firstTime = True;


for i in range(length - 1):

    if "$~$" in words[i]:
        words[i] = words[i].rstrip('$~$')
        if (firstTime):
            firstTime = False
            fh.write(words[i])
            fh.write('\n')
        else:
            fh.write('\n')
            fh.write(words[i])
            fh.write('\n')
    else:
        fh.write(words[i] + " ")

fh.close()
