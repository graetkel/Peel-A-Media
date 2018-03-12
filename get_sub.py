import spacy
nlp = spacy.load('en')
def getSub( arg1 ):
    doc=nlp(arg1)
    sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj" or tok.dep_ == "ROOT" or tok.dep_ == "nsubjpass" or tok.dep_ == "dobj" or tok.dep_ == "pobj") ]
    return sub_toks

sent = "does he talk about sports"
print(getSub(sent))