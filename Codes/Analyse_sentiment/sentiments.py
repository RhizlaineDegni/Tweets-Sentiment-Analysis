"""
RECUPERATION DES DATA POUR LES DEUX TOURS
"""
# dump(table, open('path/nom','wb'))

from pickle import load
from pickle import dump
from operator import itemgetter
import sentiment_analyser2 as sa 
import numpy as np
import pandas as pd

# import data
data = load(open('../data/dataframe_full','rb')) 


#%% Premier tour
def clean_timestamps(data):
    data_copy = data
    data_copy['timestamp'] = data_copy['timestamp'].apply(lambda t: int(t[:-3]))
    return data_copy

cleandata=clean_timestamps(data)
data_1=cleandata.loc[data['timestamp'] < 1492970400]
data_2=cleandata.loc[data['timestamp'] >= 1492970400]

#%% Par Candidats

# liste candidats
candidats = {'Arthaud', 'Asselineau', 'Cheminade', 'Dupont-Aignan', 'Fillon',
             'Hamon','Lassalle','Le Pen','Macron','Melenchon','Poutou'}

# on crée un dataframe par candidat
def createdf(tour,candidat):
    data=[]
    if tour==1:
        data=data_1
    if tour==2:
        data=data_2

    data_candidat_1 = dict()
    for c in candidats:
        data_candidat_1[c] = data.loc[data[c]==1]
        # il faut réinitialiser les index à 0
        data_candidat_1[c]['index'] = range(data_candidat_1[c].shape[0])
        data_candidat_1[c] = data_candidat_1[c].reset_index(drop=True)

    data_candidat_2=[]
    if tour==1:
        for candidat in candidats:  
            data_candidat_2=data_candidat_1[candidat]
            data_candidat_2['polarity']=list(map(lambda x: sa.sentiment_analyser(x)[0], data_candidat_2['text']))
            data_candidat_2['subjectivity']=list(map(lambda x: sa.sentiment_analyser(x)[1], data_candidat_2['text']))
            dump(data_candidat_2, open('./Premier_tour/'+candidat+'_1','wb'))
    if tour==2:
        for candidat in candidats:  
            data_candidat_2=data_candidat_1[candidat]
            data_candidat_2['polarity']=list(map(lambda x: sa.sentiment_analyser(x)[0], data_candidat_2['text']))
            data_candidat_2['subjectivity']=list(map(lambda x: sa.sentiment_analyser(x)[1], data_candidat_2['text']))
            dump(data_candidat_2, open('./Deuxieme_tour/'+candidat+'_2','wb'))

createdf(1,candidats)
createdf(2,candidats)