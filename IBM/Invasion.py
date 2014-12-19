'''
Created on 18.12.2014

@author: fberg
'''
from Individual import *
import math as ma

class Invasion:
    
    def __init__(self,N,r,d,K,b1,b2,m):
        self.resident = Individual(N,b1)
        self.invader = Individual(3,b2)
        self.r = r
        self.d = d
        self.K = K
        self.m = m
        self.N = 0
        self.invaderExist = 0
        self.invasion = 0
        self.residentList=[self.resident,]
        self.invaderList=[self.invader,]
        
    def invade(self,runs):
        self.invaderExist = 0
        for run in range(0,runs):
            self.invasion = 0
            for a in range(0,600):
                self.getTotalNumber()
                self.resident.reproduce(self.r, self.d, self.N, self.K)
            self.invaderExist = 1
            for b in range(0,500):
                self.getTotalNumber()
                self.resident.reproduce(self.r, self.d, self.N, self.K)
                self.invader.reproduce(self.r, self.d, self.N, self.K)
            if self.invader.getIndividualNumber() > 0: self.invasion += 1
            
    def invadeTime(self):
        self.invaderExist = 0
        for a in range(0,100):
            self.getTotalNumber()
            self.resident.reproduce(self.r, self.d, self.N, self.K)
        self.invader = Individual(1,self.b2)
        self.invaderExist = 1
        tick = 1
        while self.invader.getIndividualNumber() > 0 and tick < 500000:
            self.getTotalNumber()
            self.resident.reproduce(self.r, self.d, self.N, self.K)
            self.invader.reproduce(self.r, self.d, self.N, self.K)
        return ma.log10(tick)
    
    def mutate(self):
        for i in self.residentList:
            numberIndividuals = i.getIndividualNumber()
            numberMutants = np.random.poisson(numberIndividuals *self.m / self.K)
            if numberMutants > numberIndividuals: numberMutants = numberIndividuals
            for k in range(0,numberMutants):
                mutant = i.getMutant()
                if i.getIndividualNumber <= 0:
                    self.residentList.remove(i)
                self.residentList.append(mutant)
        for i in self.invaderList:
            numberIndividuals = i.getIndividualNumber()
            numberMutants = np.random.poisson(numberIndividuals *self.m / self.K)
            if numberMutants > numberIndividuals: numberMutants = numberIndividuals
            for k in range(0,numberMutants):
                mutant = i.getMutant()
                if i.getIndividualNumber <= 0:
                    self.residentList.remove(i)
                self.invaderList.append(mutant)
        
    def mutationDevelopment(self,type):
        bdevr = []
        bdevi = []
        for c in range(0,150000):
            self.getTotalNumber()
            for r in self.residentList: r.reproduce(self.r,self.d,self.N,self.K)
            for i in self.invaderList: i.reproduce(self.r,self.d,self.N,self.K)
            if c > 30000: self.mutate()
            for r in self.residentList: bdevr.append([c, r.getB()])
            for i in self.invaderList: bdevi.append([c, i.getB()])
        if type == 'resident': return bdevr
        if type == 'invader' : return bdevi
            
    def getInvasionProp(self,runs):
        return self.invasion/runs
                
    def getTotalNumber(self):
        self.N = 0
        for i in self.residentList:
            individualNumber = i.getIndividualNumber()
            self.N += individualNumber
        if self.invaderExist == 1: 
            for i in self.invaderList:
                individualNumber = i.getIndividualNumber()
                self.N += individualNumber
        return self.N
    
    def getResidentNumber(self):
        individualNumber = 0
        for i in self.residentList:
            individualNumber = i.getIndividualNumber()
        return individualNumber
    
    def getInvaderNumber(self):
        individualNumber = 0
        for i in self.invaderList:
            individualNumber = i.getIndividualNumber()
        return individualNumber