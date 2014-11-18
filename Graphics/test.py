'''
Created on 14.11.2014

@author: Franziska Berg
'''
import numpy as np
import math as ma
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.tri as tri

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
bvalues = np.logspace(0.1,20,100)
bvalues.sort()

#Create result Array
result = np.zeros((100*100,3))
row = 0

r = 1

#Fill result Array
for bR in bvalues:
    resident = residentPopulation(N, cycles, d, r, K, bR)
    for bI in bvalues:
        fitness = invaderFitness(resident, d, r, K, bI)
        result[row,:] = [bR, bI, fitness]
        row += 1
    print r
    r += 1

print result

xi, yi = np.meshgrid(result[:,0], result[:,1])
plt.figure()
plt.pcolor(xi,yi,z = result[:,2], cmap='PuBu_r')
plt.colorbar()
plt.show()
