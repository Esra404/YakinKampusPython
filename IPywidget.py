import ipywidgets as widgets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tab = widgets.Tab()
placeholder=widgets.Label()                       # şimdilik boş 
tab.children = [placeholder,placeholder,placeholder]
tab.set_title(0, "Upload")
tab.set_title(1, "Describer")
tab.set_title(2, "Plotter")
print(tab)
up=widgets.FileUpload(accept='',multiple=False)
print(up)
out=widgets.Output(layout={'border':'lpx solid black'})
tab.children=[up,out,out]
print(tab)
eraser=widgets.SelectMultiple(
    options=['tab','"'],
    value=['tab'],
    description='   Eraser:',
    disabled=False
)
print(eraser)