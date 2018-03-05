
import os
#import get_transcript https://www.youtube.com/watch?v=JMP8_HioNqU --file ~/Desktop



TEXT = raw_input("enter a file name: ")
#words = file(TEXT, "r").read()

os.system('python get_transcript.py ' + TEXT + ' --file ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
os.system('python get_wsd.py tempTranscript.txt')
