
import os
import get_kid_rating as kidRating
import mapTranscript as transcript
#Try this link to test make sure there is no tempTranscript file
#https://www.youtube.com/watch?v=qhHmNaHete0
path = '../Peel-A-Media/'
text = input("enter the youtube url: ")
path = path + text
TEXT = open(path, 'r').read()
sentences = transcript.getSentence(transcript, TEXT)
print(sentences)

print(kidRating.getRating(TEXT, transcript.getLastTime(transcript)))








#try:
#    os.system('python get_transcript.py ' + TEXT + ' --file ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
#except:
#    os.system('python get_transcript.py ' + TEXT + ' --overwrite ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')


#print("This is Irene's stuff \n")
#os.system('python get_wsd.py tempTranscript.txt')


#print("This is Casey's stuff \n")
#os.system('python getSynParse.py')



#os.remove("tempTranscript.txt")
#print("Temp File Removed!")
