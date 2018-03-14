
import os
import get_kid_rating as kidRating
import mapTranscript as transcript
#Try this link to test make sure there is no tempTranscript file
#https://www.youtube.com/watch?v=qhHmNaHete0
path = '../Peel-A-Media/'

print("Welcome to Peel A Media")
print("Please choose one of the following numbers")
print("1 Youtube URL")
print("2 Text File")

options = input("Please put the following number here: ")
# text = 'https://www.youtube.com/watch?v=qhHmNaHete0'
# path = path + text

#https://www.youtube.com/watch?v=IAbFlWQnlD4
#When does he cut the chicken

#https://www.youtube.com/watch?v=4dr5lN1jqRE
#When does he talk about clauses

#JohnWickBabaYaga.txt
#where is the car
#cuss words

accept = False

print("")

if (options == '1'):
    link = input("Please enter the Youtube URL here: ")
    print("")

    try:
     os.system('python get_transcript.py ' + link + ' --file ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
    except:
     os.system('python get_transcript.py ' + link + ' --overwrite ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')

    os.system('python secondsToMinutes.py')


    path = path + "tempTranscript.txt"
    TEXT = open(path, 'r').read()
    accept = True

elif (options == '2'):
    text = input("Please enter your transcript text file here: ")
    print ("")
    path =  path + text
    TEXT = open(path, 'r').read()
    accept = True

else:
    print("Sorry input was invalid please try again")
    accept = False







#
# path = path + "tempTranscript.txt"
# TEXT = open(path, 'r').read()
#
#
# # TEXT = open('tempTranscript.txt', 'r')

choices = ''

if (accept):
    while choices != 'quit':
    # Ask the user for a name.

        print("Please choose one of the following options")
        print("1 Find timestamps")
        print("2 Get Child Rating")
        print("3 Find all censored words")

        choices = input("Please enter number, or enter 'quit': ")


        if (choices == '1'):
            print("")
            question = input("What timestamp would you like to find: ")
            # print("---")
            # print(question)
            # print("----")
            sentences = transcript.getSentence(transcript,TEXT, question)
            print(sentences)
        if (choices == '2'):
            print("")
            print("Score rating system 0 to 10")
            print("Bad Rating Score: " + str(kidRating.getRating(TEXT, transcript.getLastTime(transcript))))
        if (choices == '3'):
            print("")
            transcript.getSentence(transcript, TEXT, "")
            print(transcript.getBadSen())

        print("")









if (accept):
    if (options == '1'):
        os.remove("tempTranscript.txt")

    print("")
    print ("Thank You For Using Our Program")

# sentence = ""
# for sen in transcript.getBadSen():
#   sentence = sentence + sen
# print("Child rating scale out of 10")
# print("0 is perfectly word friendly for children")
# print("10 is do not let them watch")
# print("Child rating is " + str(kidRating.getRating(TEXT, transcript.getLastTime(transcript))))
# print("sentences that contain bad words are found at:")
# print(sentence)










#print("This is Irene's stuff \n")
#os.system('python get_wsd.py tempTranscript.txt')


#print("This is Casey's stuff \n")
#os.system('python getSynParse.py')



# os.remove("tempTranscript.txt")
#print("Temp File Removed!")
