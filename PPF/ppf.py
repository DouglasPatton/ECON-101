import numpy as np
from bokeh.io import push_notebook, show, output_notebook; 
from bokeh.plotting import figure; 
from bokeh.layouts import layout
from bokeh.models import ColumnDataSource
output_notebook()

class ppf(object):
    '''takes 2 factories, a shared resource/input, and steps between integer
    value of resource and computes all production possibilities
    ''' 
    
    def __init__(self,factoryX,factoryY,resource,step=10):
        self.Lx=np.linspace(0,resource,resource*step+1)
        self.Ly=resource-self.Lx
        factoryX.produce(self.Lx)
        factoryY.produce(self.Ly)
        self.Qx=factoryX.outputs
        self.Qy=factoryY.outputs
        
        source = ColumnDataSource(data=dict(Lx=self.Lx, Ly=self.Ly, Qx=self.Qx, Qy=self.Qy))#setup data for bokeh brushing
        TOOLS = "box_select,lasso_select,help"
        self.ppf=figure(tools=TOOLS, title='PPF', plot_width=500, plot_height=500)
        self.ppf.xaxis.axis_label = 'Qx'
        self.ppf.yaxis.axis_label = 'QY'
        self.ppf.circle('Qx','Qy', source=source)
        
        self.Fx=figure(tools=TOOLS, title='Production of X', plot_width=250, plot_height=250)
        self.Fx.xaxis.axis_label = 'L to X'
        self.Fx.yaxis.axis_label = 'Qx'
        self.Fx.circle('Lx','Qx', source=source)
        
        self.Fy=figure(tools=TOOLS, title='Production of Y', plot_width=250, plot_height=250)
        self.Fy.xaxis.axis_label = 'L to Y'
        self.Fy.yaxis.axis_label = 'Qy'
        self.Fy.circle('Ly','Qy', source=source)
        

        
    def ppfplot(self): #plots the ppf
        show(self.ppf)
        
    def fullplot(self):
        self.l=layout(children=[self.ppf,[self.Fx,self.Fy]],
        sizing_mode='fixed')
        show(self.l)
        
