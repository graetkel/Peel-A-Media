
import os

#Try this link to test make sure there is no tempTranscript file
#https://www.youtube.com/watch?v=qhHmNaHete0

TEXT = input("enter the youtube url: ")
#words = file(TEXT, "r").read()

print("Creating a temp file called tempTranscript ...")

try:
    os.system('python get_transcript.py ' + TEXT + ' --file ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
except:
    os.system('python get_transcript.py ' + TEXT + ' --overwrite ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')


print("This is Irene's stuff \n")
os.system('python get_wsd.py tempTranscript.txt')


print("This is Casey's stuff \n")
os.system('python getSynParse.py')



os.remove("tempTranscript.txt")
print("Temp File Removed!")
