# -*- coding: utf-8 -*-

# PWZN Projekt 5
# Paweł Dębowski

from bokeh.plotting import figure, show
from bokeh.layouts import layout
from bokeh.models import  HoverTool, LinearColorMapper, ColumnDataSource, RangeSlider
from bokeh.palettes import plasma
from bokeh.transform import transform
import numpy as np
  
import pandas as pd
filename ='c:/Users/test/Desktop/PWZN/5/ZakazeniaPL.csv'
data = pd.read_csv(filename, sep=';')

data = ColumnDataSource(data)
iksy = np.arange(266)
data.data["iksy"] = iksy
maksimum = 28e3
daty = data.data['Data']

hover = HoverTool(tooltips=[
    ("Data", "@Data"),
    ("Dzień", "$index"),
    ("Nowe przypadki", "@Nowe_przypadki"),
    ("Zgony", "@Zgony"),
])

mapper = LinearColorMapper(palette=plasma(256), low=0, high=maksimum)

p = figure(width=1000,height=500, x_range=(0, 265), y_range=(0, maksimum), tools=[hover])
p.toolbar.logo = None

p.title.text = 'Covid19 w Polsce od 03.03.2021 do 23.11.2021'
p.xaxis.axis_label = 'Dzień pandemii'
p.yaxis.axis_label = 'Liczba jednostek'

p.line(x='iksy', y='Nowe_przypadki', source=data)
p.circle('iksy', 'Nowe_przypadki', size=5, source=data, fill_color=transform('Nowe_przypadki', mapper))
p.x('iksy', 'Zgony', size=5, source=data, color = 'red')

range_slider = RangeSlider(
    title="Przytnij zakres dni",
    start=0,
    end=265,
    step=1,
    value=(p.x_range.start, p.x_range.end),
)
  
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)
  
layout = layout([range_slider], [p])
show(layout)