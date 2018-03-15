#Made by group 3 in TCSS456
#Casey Anderson, Irene Fransiga, and Keldon Fischer
#Winter of 2018

import os
import get_kid_rating as kidRating
import mapTranscript as transcript


#Sample Links and Text
#https://www.youtube.com/watch?v=IAbFlWQnlD4
#When does he cut the chicken

#https://www.youtube.com/watch?v=4dr5lN1jqRE
#When does he talk about clauses

#JohnWickBabaYaga.txt
#where is the car
#cuss words




path = '../Peel-A-Media/'


# Intro

print("Welcome to Peel A Media")
print("Please choose one of the following numbers")
print("1 Youtube URL")
print("2 Text File")

options = input("Please put the following number here: ")

accept = False

print("")

# Figures out if the user want to use a Youtube Link or a Text File

# Option one lets the user type in there youtube url, our program will then
# turn it into a transcript, that we will use for the rest of the program
if (options == '1'):
    link = input("Please enter the Youtube URL here: ")
    print("")

    # We used Gordon's get_transcript here, please open get_transcript.py to view
    # Gordon's code. Also we did modify the code to work better with our code.
    try:
     os.system('python get_transcript.py ' + link + ' --file ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
    except:
     os.system('python get_transcript.py ' + link + ' --overwrite ~/Documents/game\ stuff/Assignment\ 1/Peel-A-Media')
    # End of the code we used from Gordon

    os.system('python secondsToMinutes.py')


    path = path + "tempTranscript.txt"
    TEXT = open(path, 'r').read()
    accept = True

# Option two grabs the transcript provided and uses that for the program
elif (options == '2'):
    text = input("Please enter your transcript text file here: ")
    print ("")
    path =  path + text
    TEXT = open(path, 'r').read()
    accept = True

# If neither option 1 or 2 is selected then end the program
else:
    print("Sorry input was invalid please try again")
    accept = False



choices = ''

# List all possible commands for the transcript
if (accept):
    # If the user does type quit then the program will keep on showing the user
    # all of the possible commands to use on the transcript.
    while choices != 'quit':
    # Ask the user for a name.

        print("Please choose one of the following options")
        print("1 Find timestamps")
        print("2 Get Child Rating")
        print("3 Find all censored words")

        choices = input("Please enter number, or enter 'quit': ")

        # If user chooses one then user can then type in something that they are
        # looking for in the video, our program will then find all time stamps
        # with what the user is looking for.
        if (choices == '1'):
            print("")
            question = input("What timestamp would you like to find: ")
            sentences = transcript.getSentence(transcript,TEXT, question)
            print(sentences)
        # If user chooses two then it will return a score from 0 to 10 depending
        # on how many censored words were used in the transcript over a given
        # time.
        if (choices == '2'):
            print("")
            print("Score rating system 0 to 10")
            print("Bad Rating Score: " + str(kidRating.getRating(TEXT, transcript.getLastTime(transcript))))
        # If user chooses three then it will return all the timestamps where the
        # transcript says any censored words.
        if (choices == '3'):
            print("")
            transcript.getSentence(transcript, TEXT, "")
            print(transcript.getBadSen())

        print("")




# This end the program and gets rid of any temp files
if (accept):
    # If the user uses a url our program makes a temp file for the transcript
    # this function deletes the tempTranscript after the user types quit.
    if (options == '1'):
        os.remove("tempTranscript.txt")

    print("")
    print ("Thank You For Using Our Program")
