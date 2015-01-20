'''
Created on 01.12.2014

@author: fberg
'''
from Invasion import *
import matplotlib.pyplot as plt

d = 0.05
r = 5
N1 = 200
N2 = 3
N = 200
K = 200
runs = 10
bvalues = np.logspace(0, 1.3, 200)
bvalues.sort()
bposition = len(bvalues)
invasion = Invasion()

# Create result Arrays
result = np.zeros((200, 200))

for a in range(0, bposition):
    b1 = bvalues[a]
    for b in range(0, bposition):
        b2 = bvalues[b]
        result[a, b] = invasion.runInvasion(10, 500, 500, N1, N2, r, d, K, b1, b2)
        
y, x = np.meshgrid(bvalues, bvalues)
z = result

plt.pcolor(x, y, z, cmap='Greys')
plt.colorbar()
plt.xscale('log')
plt.yscale('log')
plt.xlim(0, 19.95)
plt.ylim(0, 19.95)
plt.axvline(x=2.533333333, color='k', linestyle='--')
plt.axhline(y=2.533333333, color='k', linestyle='--')
tick = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]
plt.xticks(tick, tick)
plt.yticks(tick, tick)
plt.xlabel('Resident density-compensation strategy b')
plt.ylabel('Invading density-compensation strategy b')
plt.title('(a) Invasion probability')
plt.savefig('Result3a.png')

result = np.zeros((200,200))
result2 = np.zeros((200,200))

for a in range(0, bposition):
    b1 = bvalues[a]
    for b in range(0, bposition):
        b2 = bvalues[b]
        resulta=invasion.runCoexistence(N, r, d, K, b1, b2)
        result[a,b] = resulta[0]
        result2[a,b] = resulta[1]

z = result

plt.clf()
plt.pcolor(x, y, z, cmap='jet')
plt.colorbar()
plt.xscale('log')
plt.yscale('log')
plt.xlim(0,19.95)
plt.ylim(0,19.95)
plt.xticks(tick,tick)
plt.yticks(tick,tick)
plt.xlabel('Resident density-compensation strategy b')
plt.ylabel('Invading density-compensation strategy b')
plt.title('(b) Log10 time until competitive exclusion')
plt.savefig('Result4a.png')

z = result2

plt.clf()
plt.pcolor(x, y, z, cmap='Greys')
plt.xscale('log')
plt.yscale('log')
plt.xlim(0, 19.95)
plt.ylim(0, 19.95)
plt.xticks(tick, tick)
plt.yticks(tick, tick)
plt.xlabel('Resident density-compensation strategy b')
plt.ylabel('Invading density-compensation strategy b')
plt.title('(c) Surviving species of competitive exclusion')
plt.savefig('Result4a2.png')

N = 1000
K = 1000
m = 0.3
b1 = 0.9
b2 = 5.4

bValues = invasion.runMutationdevelopment_coexistingCommunity(N, r, d, K, b1, b2, m)
yearsr, bvaluesr = zip(*bValues[:,0:1])
yearsi, bvaluesi = zip(*bValues[:,-1])

plt.clf()
plt.plot(yearsr,bvaluesr,marker='.',linestyle='')
plt.plot(yearsi,bvaluesi,marker='.',linestyle='',color='r')
plt.xlabel('Time')
plt.ylabel('Density-compensation strategy b')
plt.title('(a) Collapse of a coexisting community')
plt.axvline(x=30000, color='k', linestyle='--')
plt.savefig('Result5.png')

b1 = 0.5
b2 = 6

bValues = invasion.runMutationdevelopment_independentPopulations(N, r, d, K, b1, b2, m)
yearsr, bvaluesr = zip(*bValues[:,0:1])
yearsi, bvaluesi = zip(*bValues[:,-1])

plt.clf()
plt.plot(yearsr,bvaluesr,marker='.',linestyle='')
plt.plot(yearsi,bvaluesi,marker='.',linestyle='',color='r')
plt.xlabel('Time')
plt.ylabel('Density-compensation strategy b')
plt.title('(b) Convergent evolution of independent populations')
plt.axvline(x=30000, color='k', linestyle='--')
plt.savefig('Result6.png')

