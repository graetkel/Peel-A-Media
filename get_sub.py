import spacy
nlp = spacy.load('en')
def getSub( arg1 ):
    doc=nlp(arg1)
    for tok in doc: 
        print(tok.dep_)
    #return sub_toks

sent = "does he talk about sports"
getSub(sent)