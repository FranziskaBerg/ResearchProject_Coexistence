'''
Created on 27.11.2014

@author: Franziska Berg
'''
import numpy as np
from copy import deepcopy

class Individual:
    
    def __init__(self,N,b):
        self.number = N
        if b == 0:
            self.b_value = np.random.normal(0,15)
            if self.b_value < 0.17:
                self.b_value = 0.17
        else:
            self.b_value = b
        
    def reproduce(self,r,d,N,K):
        poisson = self.number*r*(1-d)/(1+(r-1)*(N/K)**self.b_value)
        self.number = np.random.poisson(poisson)
        
    def getRep(self,r,d,N,K):
        rep = r*(1-d)/(1+(r-1)*(N/K)**self.b_value)
        return rep
    
    def getMutant(self):
        self.number -= 1
        newMutant = deepcopy(self)
        newMutant.number = 1
        newMutant.b_value = self.b_value + np.random.normal()
        if newMutant.b_value < 0.17:
            newMutant.b_value = 0.17
        return(newMutant)
        
    def getIndividualNumber(self):
        return self.number
    
    def getB(self):
        return self.b_value
    

            