
import sys
sys.path.append('../')


from pickle import load
from pickle import dump
from operator import itemgetter
import sentiment_analyser as sa 
import sentiments as s
import numpy as np
import pandas as pd
import util as ut
from math import pi
import datetime as dt

import time as t

from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.layouts import gridplot


def sentiment_pondered(data):
    moy=np.average(data['polarity'], weights = data['subjectivity'])
    return moy

def pie(list):
    data = pd.Series(list).reset_index(name='value').rename(columns={'index':'candidat'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(list)]

    p = figure(plot_height=500, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@candidat: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='candidat', source=data)

    p.axis.axis_label=None
    p.axis.visible=False
    p.grid.grid_line_color = None

    show(p)
    
#pie(communaute)
#pie(communaute_perc)
#pie(petit)
#pie(grand)

def axis_day(day):
    x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in day]
    return(x)

def popularity_plot(list):
    p = figure(plot_width=600, plot_height=600, title="My Line Plot",x_axis_type="datetime")
    c=0
    color=['#3C69E7','#84DE02','#FF0800','#9400D3', '#FFAA1D','black']
    for i in list:
        str_i=i
        i=eval(i)
        it=i.groupby('day', as_index=False).sum()
        it['popularity']=it['polarity']*it['subjectivity']
        p.line(axis_day(it['day']), it['popularity'], line_width=2, color=color[c],legend=str_i, muted_color='grey', muted_alpha=0.2)
        c=c+1
    p.legend.location = "top_left"
    p.legend.click_policy="mute"    
    show(p)


#popularity_plot(grand_df)
#popularity_plot(petit_df)
