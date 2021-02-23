# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:06:35 2018

@author: PC de Antoine
"""

import re
from pickle import load



#%% import data (et clean timestamps)
def import_data(file_path='./data/dataframe_full'):
    data = load(open(file_path,'rb')) 
    clean_timestamps(data)
    return data


#%% on convertit les timestamp en int et en secondes
def clean_timestamps(data):
    data['timestamp'] = data['timestamp'].apply(lambda t: int(t[:-3]))


#%% on ne garde que les tweets jusqu'au 1er tour
def premier_tour(data):
    return data.loc[data['timestamp'] < 1492970400]


#%% on découpe le dataframe par jour
def daily_data(data):
    days = sorted(list(set(data['day'].values)))
    return [ data.loc[data['day']==day] for day in days ]


#%% on crée un dataframe par candidat
def candidats_data(data):
    candidats = {'Arthaud', 'Asselineau', 'Cheminade', 'Dupont-Aignan', 'Fillon',
             'Hamon','Lassalle','Le Pen','Macron','Melenchon','Poutou'}
    data_candidat = dict()
    for c in candidats:
        data_candidat[c] = data.loc[data[c]==1]
        # il faut réinitialiser les index à 0
        data_candidat[c]['index'] = range(data_candidat[c].shape[0])
        data_candidat[c] = data_candidat[c].reset_index(drop=True)
    return data_candidat


#%% locations
def rename_loc(dataframe, villes=["PARIS","MARSEILLE","LYON","TOULOUSE","NICE","NANTES","MONTPELLIER","STRASBOURG","BORDEAUX","LILLE"]):
    # on remplace None par . et on met en majuscules
    dataframe.loc[:,'location'] = dataframe.location.apply(lambda v: "UNKNOWN" if v==None else v.upper())
    # on renomme ville par ville
    for ville in villes:
        regex = re.compile(ville)
        dataframe.loc[:,'location'] = dataframe['location'].map(lambda v: ville if re.search(regex,v) else v)
    # retour
    return dataframe


#%% transforme un texte en liste de mots
def to_words_list(text, stopwords, del_names=True, del_politic_words=True):
    
    # on supprime les \n
    text = text.replace('\n',';')
    
    # on split
    words = re.sub("[^\w]", " ",  text).split()
    
    # on met en minuscule
    words = list(map(lambda word:word.lower(), words))

    # on supprime les stopwords
    words = list(filter(lambda mot:mot not in stopwords, words))
    
    # on vire les accents
    words = list(map(lambda mot: mot.encode('ascii','ignore').decode('utf8'), words))
    
    # si del_names on supprime les noms de candidats
    if del_names:
        candidats_words = {'arthaud', 'asselineau', 'cheminade', 'dupont','fillon',
                           'aignan','hamon','lassalle','lepen', 'pen', 'macron',
                           'melenchon','poutou','francois','nathalie','nicolas',
                           'marine','emmanuel','benoit','philippe','jacque',
                           'jean','jlm','em','luc','mlp'}
        for item in candidats_words:
            words = list(filter(lambda mot: item not in mot, words))
            
    # si del_politic_words on vire les mots 'vote', 'election', etc
    if del_politic_words:
        politic_words = {'vote','election','tour','premier','deuxieme', 'second', 
                         'programme', 'elu','politique','candidat','droite',
                         'gauche','sondage','president','france','paris',
                         'meeting','français','gagne','perd','lr','ps','npa',
                         'debat','presidentiel'}
        for item in politic_words:
            words = list(filter(lambda mot: item not in mot, words))
    
    return words


#%% transforme un texte en liste de mots [DEPRECATED]
def text_to_list_old(text, stopwords_path='./stopwords', del_maj=False, del_hashtags=False, del_mentions=True, hashtag_to_text=True, del_names=True, del_politic_words=True):
    
    """ stopwords_path : le chemin où sont situés les stopwords. """
    
    # les symboles de ponctuation et les stopwords
    ponctuation = '!" $%&()*+,-./:;<=>? [\\]^_`{|}~'
    stopwords = load(open(stopwords_path, 'rb'))
    
    # on supprime les \n et les ’
    text = text.replace('\n','')
    text = text.replace("’","'")
    
    # on split suivant les espaces et les ponctuations non suivies d'un espace
    words = re.split('(?=[?,;:.!?][a-z])| ', text)
    
    # on supprime la ponctuation
    words = list(map(lambda word:word.translate(str.maketrans('','',ponctuation)), words))
    # on supprime les mots vides
    words = list(filter(lambda mot:mot!='', words))
    # si del_maj on supprime les noms propres (commencent par une maj)
    if del_maj:
        words = list(filter(lambda mot:mot[0].islower(), words))
    # on met en minuscule
    words = list(map(lambda word:word.lower(), words))
    # on supprime les particules apostrophes (d', t', etc)
    def delete_particles(mot): # fonction qui supprime les particules apostrophes d'un mot
        if re.match("[cdjlmnst]'(.)*", mot) != None: return mot[2:]
        else: return mot
    words = list(map(delete_particles, words))
    # on supprime les stopwords
    words = list(filter(lambda mot:mot not in stopwords, words))
    # si del_hashtags on supprime les hashtags
    if del_hashtags:
        words = list(filter(lambda mot:not (mot.startswith('#')), words))
    # si hashtag_to_text on garde les hashtags mais on enlève le symbole '#'
    if hashtag_to_text:
        words = list(map(lambda mot: mot.replace('#',''), words))
    # si del_mentions on supprime les mentions
    if del_mentions:
        words = list(filter(lambda mot:not (mot.startswith('@')), words))
    # on supprime les liens web (commencent par http)
    words = list(filter(lambda mot: not mot.startswith('http'), words))
    # on vire les accents
    words = list(map(lambda mot: mot.encode('ascii','ignore').decode('utf8'), words))
    # si del_names on supprime les noms de candidats
    if del_names:
        candidats_words = {'arthaud', 'asselineau', 'cheminade', 'dupont','fillon',
                           'aignan','hamon','lassalle','lepen', 'pen', 'macron',
                           'melenchon','poutou','francois','nathalie','nicolas',
                           'marine','emmanuel','benoit','philippe','jacque',
                           'jean','jlm','em','luc'}
        for item in candidats_words:
            words = list(filter(lambda mot: item not in mot, words))
    # si del_politic_words on vire les mots 'vote', 'election', etc
    if del_politic_words:
        politic_words = {'vote','election','tour','premier','deuxieme', 'second', 
                         'programme', 'elu','politique','candidat','droite',
                         'gauche','sondage','president','france','paris',
                         'meeting','français','gagne','perd','lr','ps','npa',
                         'debat','presidentiel'}
        for item in politic_words:
            words = list(filter(lambda mot: item not in mot, words))
    
    return words