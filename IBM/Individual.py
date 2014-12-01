'''
Created on 27.11.2014

@author: Franziska Berg
'''
import random
import numpy as np

class Individual:
    
    def __init__(self):
        self.number = 1
        self.b_value = random.uniform(0.17,15)
        
    def getOffspring(self,r,d,Nto,Kto):
        poisson = r*(1-d)/(1+(r-1)*(Nto/Kto)**self.b_value)
        self.number += np.random.poisson(poisson)
        return self
    
    def getIndividualNumber(self):
        return self.number