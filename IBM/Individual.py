'''
Created on 27.11.2014

@author: Franziska Berg
'''
import random

class Individual:
    
    def __init__(self):
        self.number = 1
        self.b_value = random.uniform(0.17,15)
        
    def getOffspring(self,r,d,K):
        self.number += self.number*r*(1-d)/(1+(r-1)*(self.number/K)**self.b_value)
        return self
    
    def getIndividualNumber(self):
        return self.number