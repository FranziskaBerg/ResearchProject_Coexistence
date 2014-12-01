'''
Created on 27.11.2014

@author: Franziska Berg
'''
from Individual import *

class Population:
    
    def __init__(self,N,r,d,K):
        self.individuals = []
        self.r = r
        self.d = d
        self.K = K
        for individual in range(1,N+1):
            individual = Individual()
            self.individuals += [individual,]
        print self.individuals
    
    def updatePopulation(self):
        N = len(self.individuals)
        for i in range(0,N):
            individual = self.individuals[i]
            print i, individual.getIndividualNumber()
            individual = individual.getOffspring(self.r,self.d,self.K)
            self.individuals[i] = individual
            
    def getPopulationSize(self):
        N = len(self.individuals)
        individualN = 0
        for i in range(0,N):
            individual = self.individuals[i]
            individualN += individual.getIndividualNumber()
        return individualN
