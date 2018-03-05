
import os

#Try this link to test make sure there is no tempTranscript file
#https://www.youtube.com/watch?v=qhHmNaHete0

TEXT = raw_input("enter a file name: ")
#words = file(TEXT, "r").read()

os.system('python get_transcript.py ' + TEXT + ' --file ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
os.system('python get_wsd.py tempTranscript.txt')
