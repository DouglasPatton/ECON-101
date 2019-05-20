import numpy as np

class factory(object):
    '''makes a factory object and produce(input) computes inputs and outputs'''
    
    def __init__(self, exponent=1, constant=1):
        self.exponent = exponent
        self.constant=constant
        self.inputs=0
        self.outputs=0
        
    def produce(self, factor_input):
        self.inputs=factor_input
        self.outputs=np.array(self.constant*(self.inputs**self.exponent))

        
    

        
        
        
