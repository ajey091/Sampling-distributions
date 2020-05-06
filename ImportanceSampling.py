import scipy.stats
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np 
from random import  uniform


x = np.linspace(0,1,100)
y = x**-0.5*np.exp(-x)

fig,ax = plt.subplots(1)

numx = []
numy = []

n = 5000
for _ in range(n):
    numx.append(uniform(0, 1))
    numy.append(uniform(0, 1))

    
plt.plot(numx,numy,'k.',linewidth=1)
plt.plot(x,y,linewidth=4)
rect = patches.Rectangle((0,0),1,1,linewidth=3,edgecolor='r',facecolor='none')

ax.add_patch(rect)
plt.show()

MCintegral = sum([i**3 > j for i, j in zip(numx, numy)])/n
truthint = 0.25

print (f'Truth = {truthint}, Monte Carlo value = {MCintegral}')