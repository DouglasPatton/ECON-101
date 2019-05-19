import numpy as np

class factory1:
    '''makes a factory object and computes inputs and outputs'''
    
    def __init__(self, exponent=1, constant=1, max_input=5, steps=5):
        self.exponent = exponent
        self.constant=constant
        self.max_input=max_input
        self.input=np.linspace(0,max_input,steps)
        self.output=constant*(self.input**exponent) 
        
        
        
