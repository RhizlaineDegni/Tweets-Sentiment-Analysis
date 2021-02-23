"""
RUN SENTIMENTS.PY POUR CREER LES DATAS AVANT
"""

from pickle import load
import numpy as np



Melenchon_1 = load(open('./Premier_tour/Melenchon_1','rb')) 
Lassalle_1 =  load(open('./Premier_tour/Lassalle_1','rb')) 
Poutou_1 =  load(open('./Premier_tour/Poutou_1','rb')) 
Hamon_1 =  load(open('./Premier_tour/Hamon_1','rb')) 
Asselineau_1 =  load(open('./Premier_tour/Asselineau_1','rb'))
Arthaud_1 =  load(open('./Premier_tour/Arthaud_1','rb')) 
Cheminade_1 =  load(open('./Premier_tour/Cheminade_1','rb')) 
Dupont_Aignan_1 =  load(open('./Premier_tour/Dupont-Aignan_1','rb')) 
Fillon_1 =  load(open('./Premier_tour/Fillon_1','rb'))
LePen_1 =  load(open('./Premier_tour/Le Pen_1','rb')) 
Macron_1 =  load(open('./Premier_tour/Macron_1','rb')) 

from sentiment_visualisation import sentiment_pondered


communaute = {
        'Melenchon_1' : sentiment_pondered(Melenchon_1)*np.shape(Melenchon_1)[0],
        'Lassalle_1' : sentiment_pondered(Lassalle_1)*np.shape(Lassalle_1)[0],
        'Poutou_1' : sentiment_pondered(Poutou_1)*np.shape(Poutou_1)[0],
        'Hamon_1' : sentiment_pondered(Hamon_1)*np.shape(Hamon_1)[0],
        'Arthaud_1' : sentiment_pondered(Arthaud_1)*np.shape(Arthaud_1)[0],
        'Cheminade_1' : sentiment_pondered(Cheminade_1)*np.shape(Cheminade_1)[0],
        'Dupont_Aignan_1' : sentiment_pondered(Dupont_Aignan_1)*np.shape(Dupont_Aignan_1)[0],
        'Fillon_1' : sentiment_pondered(Fillon_1)*np.shape(Fillon_1)[0],
        'LePen_1' : sentiment_pondered(LePen_1)*np.shape(LePen_1)[0],
        'Macron_1' : sentiment_pondered(Macron_1)*np.shape(Macron_1)[0]
    }

communaute_perc = {
        'Melenchon_1' : sentiment_pondered(Melenchon_1),
        'Lassalle_1' : sentiment_pondered(Lassalle_1),
        'Poutou_1' : sentiment_pondered(Poutou_1),
        'Hamon_1' : sentiment_pondered(Hamon_1),
        'Arthaud_1' : sentiment_pondered(Arthaud_1),
        'Cheminade_1' : sentiment_pondered(Cheminade_1),
        'Dupont_Aignan_1' : sentiment_pondered(Dupont_Aignan_1),
        'Fillon_1' : sentiment_pondered(Fillon_1),
        'LePen_1' : sentiment_pondered(LePen_1),
        'Macron_1' : sentiment_pondered(Macron_1)
    }

grand = {
        'Melenchon_1' : sentiment_pondered(Melenchon_1)*np.shape(Melenchon_1)[0],
        'Hamon_1' : sentiment_pondered(Hamon_1)*np.shape(Hamon_1)[0],
        'Fillon_1' : sentiment_pondered(Fillon_1)*np.shape(Fillon_1)[0],
        'LePen_1' : sentiment_pondered(LePen_1)*np.shape(LePen_1)[0],
        'Macron_1' : sentiment_pondered(Macron_1)*np.shape(Macron_1)[0]
    }


petit = {
        'Lassalle_1' : sentiment_pondered(Lassalle_1)*np.shape(Lassalle_1)[0],
        'Poutou_1' : sentiment_pondered(Poutou_1)*np.shape(Poutou_1)[0],
        'Arthaud_1' : sentiment_pondered(Arthaud_1)*np.shape(Arthaud_1)[0],
        'Cheminade_1' : sentiment_pondered(Cheminade_1)*np.shape(Cheminade_1)[0],
        'Dupont_Aignan_1' : sentiment_pondered(Dupont_Aignan_1)*np.shape(Dupont_Aignan_1)[0]
    }

grand_df={'Melenchon_1','Macron_1','Hamon_1','Fillon_1','LePen_1'}
petit_df={'Lassalle_1','Poutou_1','Arthaud_1','Cheminade_1','Dupont_Aignan_1'}

