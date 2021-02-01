import pandas as pd
import numpy as np
import json

StopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

Vocab = {}
with open('TrainedVocab.txt') as json_file: 
        Vocab = json.load(json_file)

#Preprocessing Training
def Preprocessing (dfClassify):
    

    #Preprocessing Classification

    dfClassify = dfClassify.dropna()
    dfClassify["title"] = dfClassify["title"].str.lower()

    dfClassify["title"] = dfClassify["title"].str.replace(',', '')
    dfClassify["title"] = dfClassify["title"].str.replace(':', '')
    dfClassify["title"] = dfClassify["title"].str.replace('.', '')
    dfClassify["title"] = dfClassify["title"].str.replace(';', '')
    dfClassify["title"] = dfClassify["title"].str.replace("'", '')
    dfClassify["title"] = dfClassify["title"].str.replace('?', '')
    dfClassify["title"] = dfClassify["title"].str.replace('!', '')
    dfClassify["title"] = dfClassify["title"].str.replace('*', '')
    dfClassify["title"] = dfClassify["title"].str.replace('(', '')
    dfClassify["title"] = dfClassify["title"].str.replace(')', '')
    dfClassify["title"] = dfClassify["title"].str.replace('/', '')
    dfClassify["title"] = dfClassify["title"].str.replace("`", '')
    dfClassify["title"] = dfClassify["title"].str.replace("´", '')
    dfClassify["title"] = dfClassify["title"].str.replace("‘", '')
    dfClassify["title"] = dfClassify["title"].str.replace("’", '')
    dfClassify["title"] = dfClassify["title"].str.replace('\d+', '')

    dfClassify["title"] = dfClassify["title"].str.split(pat=' ')

    return dfClassify

def WordNotZero(word):
    
    if word not in Vocab:
        return False
    if Vocab[word][0]<=0:
        return False
    if Vocab[word][1]<=0:
        return False
    return True

def ClassifyHeadlines(dfClassify, length, AmountPositiveHeadlines, AmountNegativeHeadlines):
    
    PositiveHeadlines =[]
    NegativeHeadlines = []

    '''with open('TrainedVocab.txt') as json_file: 
    Vocab = json.load(json_file)'''
   
    
    ClassifiedPos = 0
    ClassifiedNeg = 0
    Korrekt = 0
    Falsch = 0
    p_p = 0
    p_n = 0
    n_n = 0
    n_p = 0
    
    for headlines,index in zip(dfClassify["title"],dfClassify.index):
        PNegTokens = 0.0
        PPosTokens = 0.0
        for word in headlines:
            if WordNotZero(word) == True and (len(word) > 2) and word.isalpha() and word not in StopWords:
                PNegTokens=PNegTokens +np.log(Vocab[word][0]/AmountNegativeHeadlines)
                PPosTokens=PPosTokens+np.log(Vocab[word][1]/AmountPositiveHeadlines)

                PNegTokens=PNegTokens+np.log(AmountNegativeHeadlines/length)
                PPosTokens=PPosTokens+np.log(AmountPositiveHeadlines/length)


        if PNegTokens > PPosTokens:
            ClassifiedNeg += 1
            NegativeHeadlines.append(index)
 

        elif PNegTokens < PPosTokens:
            ClassifiedPos += 1
            PositiveHeadlines.append(index)

                
                

    print("Positiv klassifiziert: ",ClassifiedPos)
    print("Negativ klassifiziert: ",ClassifiedNeg)


    return PositiveHeadlines, NegativeHeadlines






