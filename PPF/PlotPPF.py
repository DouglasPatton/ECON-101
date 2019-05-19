import numpy as np
from bokeh.io import push_notebook, show, output_notebook; 
from bokeh.plotting import figure; 
from bokeh.layouts import column
output_notebook()

def ppfdotplot(x,y):
    p.figure()
    p.circle(x,y)
    p.show()
