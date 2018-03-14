import spacy
nlp = spacy.load('en')

mySent = ["","" ,"" ,"" ,"", ""]
def getSub( arg1 ):
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
    print(mySent)
    return mySent
