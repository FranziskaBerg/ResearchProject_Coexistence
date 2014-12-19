'''
Created on 27.11.2014

@author: Franziska Berg
'''
from Individual import *

class Population:
    
    def __init__(self,N,r,d,K,m):
        self.individuals = []
        self.N = 0
        self.r = r
        self.d = d
        self.K = K
        self.m = m
        for i in range(0,N):
            self.individuals.append(Individual(1,0))
                
    def updatePopulation(self,cycle):
        for c in range(0,cycle):
            self.getPopulationSize()
            for i in self.individuals:
                i.reproduce(self.r, self.d, self.N, self.K)
            self.mutate()
        
    def mutate(self):
        for i in self.individuals:
            numberIndividuals = i.getIndividualNumber()
            numberMutants = np.random.poisson(numberIndividuals *self.m / self.K)
            if numberMutants > numberIndividuals: numberMutants = numberIndividuals
            for k in range(0,numberMutants):
                mutant = i.getMutant()
                if i.getIndividualNumber <= 0:
                    self.individuals.remove(i)
                self.individuals.append(mutant)
          
    def getPopulationSize(self):
        individualN = 0
        for i in self.individuals:
            individualN += i.getIndividualNumber()
        self.N = individualN
        return self.N
    
    def getAverageB(self):
        b = 0
        for i in self.individuals:
            b += i.getB()
        averageB = b / len(self.individuals)
        return averageB
    
    def getCriticalB(self):
        b = 2-(2/(1+(self.d-1)*self.r))
        return b