# We used the Spacy API in our code, here is a link to there site:
# https://spacy.io/api/
# Thank You Spacy for letting us use your API
import spacy

nlp = spacy.load('en')

def getSub( arg1 ):
    mySent = ["","" ,"" ,"" ,"", ""]

    doc=nlp(arg1)
    for tok in doc:
        if (tok.dep_ == "nsubj"):
            mySent[1] = tok.text
        elif (tok.dep_ == "ROOT"):
            mySent[0] = tok.text
        elif (tok.dep_ == "nsubjpass"):
            mySent[4] = tok.text
        elif (tok.dep_ == "dobj"):
            mySent[2] = tok.text
        elif (tok.dep_ == "pobj"):
            mySent[3] = tok.text
        elif (tok.dep_ == "compound"):
            mySent[5] = tok.text
    return mySent
