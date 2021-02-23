"""
RUN SENTIMENTS.PY POUR CREER LES DATAS AVANT
"""

from pickle import load
import numpy as np


Melenchon_2 = load(open('./Deuxieme_tour/Melenchon_2','rb')) 
Lassalle_2 =  load(open('./Deuxieme_tour/Lassalle_2','rb')) 
Poutou_2 =  load(open('./Deuxieme_tour/Poutou_2','rb')) 
Hamon_2 =  load(open('./Deuxieme_tour/Hamon_2','rb')) 
Asselineau_2 =  load(open('./Deuxieme_tour/Asselineau_2','rb'))
Arthaud_2 =  load(open('./Deuxieme_tour/Arthaud_2','rb')) 
Cheminade_2 =  load(open('./Deuxieme_tour/Cheminade_2','rb')) 
Dupont_Aignan_2 =  load(open('./Deuxieme_tour/Dupont-Aignan_2','rb')) 
Fillon_2 =  load(open('./Deuxieme_tour/Fillon_2','rb'))
LePen_2 =  load(open('./Deuxieme_tour/Le Pen_2','rb')) 
Macron_2 =  load(open('./Deuxieme_tour/Macron_2','rb')) 



from sentiment_visualisation import sentiment_pondered


communaute2 = {
        'Melenchon_2' : sentiment_pondered(Melenchon_2)*np.shape(Melenchon_2)[0],
        'Lassalle_2' : sentiment_pondered(Lassalle_2)*np.shape(Lassalle_2)[0],
        'Poutou_2' : sentiment_pondered(Poutou_2)*np.shape(Poutou_2)[0],
        'Hamon_2' : sentiment_pondered(Hamon_2)*np.shape(Hamon_2)[0],
        'Arthaud_2' : sentiment_pondered(Arthaud_2)*np.shape(Arthaud_2)[0],
        'Cheminade_2' : sentiment_pondered(Cheminade_2)*np.shape(Cheminade_2)[0],
        'Dupont_Aignan_2' : sentiment_pondered(Dupont_Aignan_2)*np.shape(Dupont_Aignan_2)[0],
        'Fillon_2' : sentiment_pondered(Fillon_2)*np.shape(Fillon_2)[0],
        'LePen_2' : sentiment_pondered(LePen_2)*np.shape(LePen_2)[0],
        'Macron_2' : sentiment_pondered(Macron_2)*np.shape(Macron_2)[0]
    }

communaute_perc2 = {
        'Melenchon_2' : sentiment_pondered(Melenchon_2),
        'Lassalle_2' : sentiment_pondered(Lassalle_2),
        'Poutou_2' : sentiment_pondered(Poutou_2),
        'Hamon_2' : sentiment_pondered(Hamon_2),
        'Arthaud_2' : sentiment_pondered(Arthaud_2),
        'Cheminade_2' : sentiment_pondered(Cheminade_2),
        'Dupont_Aignan_2' : sentiment_pondered(Dupont_Aignan_2),
        'Fillon_2' : sentiment_pondered(Fillon_2),
        'LePen_2' : sentiment_pondered(LePen_2),
        'Macron_2' : sentiment_pondered(Macron_2)
    }

grand2 = {
        'Melenchon_2' : sentiment_pondered(Melenchon_2)*np.shape(Melenchon_2)[0],
        'Hamon_2' : sentiment_pondered(Hamon_2)*np.shape(Hamon_2)[0],
        'Fillon_2' : sentiment_pondered(Fillon_2)*np.shape(Fillon_2)[0],
        'LePen_2' : sentiment_pondered(LePen_2)*np.shape(LePen_2)[0],
        'Macron_2' : sentiment_pondered(Macron_2)*np.shape(Macron_2)[0]
    }


petit2 = {
        'Lassalle_2' : sentiment_pondered(Lassalle_2)*np.shape(Lassalle_2)[0],
        'Poutou_2' : sentiment_pondered(Poutou_2)*np.shape(Poutou_2)[0],
        'Arthaud_2' : sentiment_pondered(Arthaud_2)*np.shape(Arthaud_2)[0],
        'Cheminade_2' : sentiment_pondered(Cheminade_2)*np.shape(Cheminade_2)[0],
        'Dupont_Aignan_2' : sentiment_pondered(Dupont_Aignan_2)*np.shape(Dupont_Aignan_2)[0]
    }

grand_df2={'Melenchon_2','Macron_2','Hamon_2','Fillon_2','LePen_2'}
petit_df2={'Lassalle_2','Poutou_2','Arthaud_2','Cheminade_2','Dupont_Aignan_2'}

