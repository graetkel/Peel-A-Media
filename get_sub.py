import spacy
nlp = spacy.load('en')
def getSub( arg1 ):
    doc=nlp(arg1)
    sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj") ]
    return sub_toks