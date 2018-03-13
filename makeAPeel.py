
import os
import get_kid_rating as kidRating
import mapTranscript as transcript
#Try this link to test make sure there is no tempTranscript file
#https://www.youtube.com/watch?v=qhHmNaHete0
path = '../Peel-A-Media/'
# text = input("enter the youtube url: ")
text = 'https://www.youtube.com/watch?v=qhHmNaHete0'
# path = path + text


try:
  os.system('python get_transcript.py ' + text + ' --file ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
except:
  os.system('python get_transcript.py ' + text + ' --overwrite ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')

os.system('python secondsToMinutes.py')

path = path + "tempTranscript.txt"

TEXT = open(path, 'r').read()
# TEXT = open('tempTranscript.txt', 'r')
sentences = transcript.getSentence(transcript,TEXT)
print(sentences)

# print(kidRating.getRating(TEXT, transcript.getLastTime(transcript)))



os.remove("tempTranscript.txt")


# print("Child rating scale out of 10")
# print("0 is perfectly word friendly for children")
# print("10 is do not let them watch")
# print("Child rating is " + str(kidRating.getRating(TEXT, transcript.getLastTime(transcript))))











#print("This is Irene's stuff \n")
#os.system('python get_wsd.py tempTranscript.txt')


#print("This is Casey's stuff \n")
#os.system('python getSynParse.py')



#os.remove("tempTranscript.txt")
#print("Temp File Removed!")
