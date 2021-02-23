# -*- coding: utf-8 -*-
"""
Created on Nov 26 2018

@author: PC de Rhizlaine

Pour analyser le sentiment d'un texte sous forme de string.
"""

from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer


def sentiment_analyser(text):
    
    blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    sentiments=blob.sentiment

    # on renvoie le résultat
    return sentiments

