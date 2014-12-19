'''
Created on 01.12.2014

@author: fberg
'''
from Population import *
from Invasion import *
import matplotlib.pyplot as plt

r_values = np.arange(1,6,0.025)
print len(r_values)
r_position = 0
d_values = np.arange(0,0.5,0.0025)
print len(d_values)
d_position = 0
N = 200
K = 200
m = 0.1


#Create result Arrays
result1 = np.zeros((200,200))
result2 = np.zeros((200,200))

for r in r_values:
    d_position = 0
    for d in d_values:
        pop = Population(N,r,d,K,m)
        pop.updatePopulation(10000)
        result1[r_position,d_position]=pop.getAverageB()
        result2[r_position,d_position]=pop.getCriticalB()-pop.getAverageB()
        d_position += 1
    r_position += 1
    
#Creates plot data
y, x = np.meshgrid(d_values,r_values)
z = result1
z2 = result2

plt.pcolor(x,y,z,cmap='afmhot')
plt.colorbar()
plt.xlabel('Intrinsic growth rate r')
plt.ylabel('Density-independent mortality d')
plt.title('(a) ESS of individual-based model')
plt.savefig("Result1.png")

plt.clf()
plt.pcolor(x,y,z2,cmap='seismic',vmin=-15,vmax=15)
plt.colorbar()
plt.xlabel('Intrinsic growth rate r')
plt.ylabel('Density-independent mortality d')
plt.title('(b) Deviation of ESS from critical b-value')
plt.savefig("Result2.png")

d = 0.05
r = 5
N = 1000
K = 1000
runs = 10
bvalues = np.logspace(0,1.3,200)
bvalues.sort()
bposition = len(bvalues)

for a in range(0,bposition):
    b1 = bvalues[a]
    for b in range(0,bposition):
        b2 = bvalues[b]
        invasion = Invasion(N,r,d,K,b1,b2,0,1)
        invasion.invade(runs)
        result1[a,b] = invasion.getInvasionProp(runs)
        result2[a,b] = invasion.invadeTime()
        print a, b
        
y, x = np.meshgrid(bvalues,bvalues)
z = result1
z2 = result2

plt.clf()
plt.pcolor(x,y,z,cmap='Greys')
plt.colorbar()
plt.xscale('log')
plt.yscale('log')
plt.xlim(0,19.95)
plt.ylim(0,19.95)
plt.axvline(x=2.533333333, color='k', linestyle='--')
tick = [2,3,4,5,6,7,8,9,10,12,15]
plt.xticks(tick,tick)
plt.yticks(tick,tick)
plt.xlabel('Resident density-compensation strategy b')
plt.ylabel('Invading density-compensation strategy b')
plt.title('(a) Invasion probability')
plt.savefig("Result3.png")

plt.clf()
plt.pcolor(x,y,z2, cmap= "jet")
plt.xscale('log')
plt.yscale('log')
plt.xlim(0,19.95)
plt.ylim(0,19.95)
plt.xticks(tick,tick)
plt.yticks(tick,tick)
plt.xlabel('Resident density-compensation strategy b')
plt.ylabel('Invading density-compensation strategy b')
plt.title('(b) Log10 time until competitive exclusion')
plt.savefig("Result4.png")

d = 0.05
r = 5
N = 1000
K = 1000
m = 0.3
b1 = 0.9
b2 = 5.4

invasion = Invasion(N,r,d,K,b1,b2,m)

bDevelopr = invasion.mutationDevelopment('resident')
yearsr, bvaluesr = zip(*bDevelopr)

bDevelopi = invasion.mutationDevelopment('invader')
yearsi, bvaluesi = zip(*bDevelopi)

plt.clf()
plt.plot(yearsr,bvaluesr,marker='o',linestyle='')
plt.plot(yearsi,bvaluesi,marker='.',linestyle='',color='r')
plt.xlabel('Time')
plt.ylabel('Density-compensation strategy b')
plt.title('(a) Collapse of a coexisting community')
plt.savefig("Result5.png")

b1 = 0.5
b2 = 6

invasion = Invasion(N,r,d,K,b1,b2,m)

bDevelopr = invasion.mutationDevelopment('resident')
yearsr, bvaluesr = zip(*bDevelopr)

bDevelopi = invasion.mutationDevelopment('invader')
yearsi, bvaluesi = zip(*bDevelopi)

plt.clf()
plt.plot(yearsr,bvaluesr,marker='o',linestyle='')
plt.plot(yearsi,bvaluesi,marker='.',linestyle='',color='r')
plt.xlabel('Time')
plt.ylabel('Density-compensation strategy b')
plt.title('(b) Convergent evolution of independent populations')
plt.savefig("Result6.png")
