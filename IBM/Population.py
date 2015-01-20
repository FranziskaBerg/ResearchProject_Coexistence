'''
Created on 27.11.2014

@author: Franziska Berg
'''
from Individual import *

class Population:
    
    def __init__(self,mutationON=False,mutationProbability=0):
        self.individuals = []
        self.mutationProbability = mutationProbability
        self.totalPopulationSize = 0
        self.mutationON = mutationON
 
    def addIndividual(self,r,d,N,b,K,resident=True):
        self.individuals.append(Individual(r,d,N,b,K,resident))
  
    def addNidenticalIndividuals(self, Number,r,d,N,b,K,resident = True):
        for i in xrange(0,Number):
            self.individuals.append(Individual(r,d,N,b,K,resident))
            
    def addExistingIndividual(self, individual):
        self.individuals.append(individual)
               
    def updatePopulation(self,cycle):
        for c in range(0,cycle):
            self.calculatePopulationSize()
            for i in self.individuals:
                i.reproduce(self.totalPopulationSize)
                if i.number <= 0:
                    self.individuals.remove(i)
            if self.mutationON:
                self.mutate()
        
    def mutate(self):
        for i in self.individuals:
            numberIndividuals = i.getIndividualNumber()
            numberMutants = np.random.poisson(numberIndividuals *self.mutationProbability / self.K)
            if numberMutants > numberIndividuals: numberMutants = numberIndividuals
            for k in range(0,numberMutants):
                mutant = i.getMutant()
                if i.getIndividualNumber <= 0:
                    self.individuals.remove(i)
                self.individuals.append(mutant)
          
    def calculatePopulationSize(self):
        individualN = 0
        for i in self.individuals:
            individualN += i.getIndividualNumber()
        self.totalPopulationSize = individualN
        
    def invaderPresent(self):
        present = False
        for i in self.individuals:
            if i.resident == False:
                present = True
        return present
                
    def residentPresent(self):
        present = False
        for i in self.individuals:
            if i.resident == True:
                present = True
        return present
                
    def residentinvaderPresent(self):
        present = False
        resident = self.residentPresent()
        invader = self.invaderPresent()
        if resident and invader:
            present = True
        return present
                     
    def getAverageB(self):
        b = 0
        for i in self.individuals:
            b += i.getB()
        averageB = b / len(self.individuals)
        return averageB
    
    def getResidentAverageB(self):
        b = 0
        individual = 0
        for i in self.individuals:
            if i.resident == True:
                b += i.b_value
                individual += 1
        if individual != 0: return b/individual
        elif individual == 0: return 0
    
    def getInvaderAverageB(self):
        b = 0
        individual = 0
        for i in self.individuals:
            if i.resident == False:
                b += i.b_value
                individual += 1
        if individual != 0: return b/individual
        elif individual == 0: return 0
    
    def getCriticalB(self):
        b = 2-(2/(1+(self.d-1)*self.r))
        return b