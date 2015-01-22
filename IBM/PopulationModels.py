'''
Created on 22.01.2015

@author: fberg
'''
from __future__ import division

class PopulationModel(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod  
    def getReproductionRatio():
        raise NotImplementedError
    
    @staticmethod
    def plotFunctionalResponse():
        raise NotImplementedError
    
    
class MSS(PopulationModel):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod      
    def getReproductionRatio(r,d,N,b,K):
        rep = r*(1-d)/(1+(r-1)*(N/K)**b)
        return rep
    
    

