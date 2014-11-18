'''
Created on 17.11.2014

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
        fit += rep
    mFit = fit.max()
    lFit = ma.log(mFit)
    fitness = lFit/T
    return fitness

def fitness (bR,bI):
    resident = residentPopulation(N, cycles, d, r, K, bR)
    fitness = invaderFitness(resident, d, r, K, bI)
    return fitness

#Sets initial Values
d = 0.05
r = 5
N = 100
K = 200
cycles = 500
bvalues = np.logspace(0.1,20,num= 100, endpoint= True)
bvalues.sort()

#Gets graphic data
x, y = np.meshgrid(bvalues,bvalues)
z = fitness(x,y)
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

plt.subplot()
plt.pcolor(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
plt.colorbar()
plt.show()