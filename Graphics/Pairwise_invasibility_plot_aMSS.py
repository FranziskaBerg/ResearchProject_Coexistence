'''
Created on 14.11.2014

@author: Franziska Berg
'''
import numpy as np
import math as ma
import matplotlib.pyplot as plt

# Definition of the Model
def MSS (d, r, N, K, b): return (1-d)*r/(1+(r-1)*(N/K)**b)

#Creates resident population
def residentPopulation (N, cycles, d, r, K, b):
    resident = []
    T = cycles +1
    for t in range (0,T):
        rep = MSS(d, r, N, K, b)
        N = N*rep
        if t >= 100:
            resident += [N,]
    return resident

#Calculates fitness of the Invader
def invaderFitness (resident, d, r, K, b):
    fit = 0
    T = len(resident)
    for t in range (0,T):
        N = resident[t]
        rep = MSS(d,r,N,K,b)
        if rep != 0: fit += ma.log(rep)
    fitness = fit/T
    return fitness

#Sets initial Values
d = 0.05
r = 5
N = 100
K = 200
cycles = 500
bvalues = np.logspace(0.1,1.3,100)
bvalues.sort()
bposition = len(bvalues)

#Create result Array
result = np.zeros((100,100))

#Fill result Array
for a in range (0,bposition):
    bR = bvalues[a]
    resident = residentPopulation(N, cycles, d, r, K, bR)
    for b in range(0,bposition):
        bI = bvalues[b]
        fitness = invaderFitness(resident, d, r, K, bI)
        result[a,b] = fitness
    
#Creates plot data
y, x = np.meshgrid(bvalues,bvalues)
z = result

#Defines the graphic
plt.pcolor(x,y,z)
plt.colorbar()
plt.xscale('log')
plt.yscale('log')
plt.xlim(0,19.95)
plt.ylim(0,19.95)
plt.show()
