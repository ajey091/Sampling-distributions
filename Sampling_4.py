import numpy as np 
import scipy.stats
import matplotlib.pyplot as plt

dist1 = scipy.stats.norm(0.0,1.0)
dist2 = scipy.stats.norm(0.0,1.0)

def checknorm(n):
    samp1 = dist1.rvs(n)
    # samp2 = dist2.rvs(n)
    res1 = scipy.stats.kstest(samp1,'norm')
    return res1[1]


n = np.linspace(2,1000,20)
stddist = []
for i in n:
    buff = []
    for _ in range(500):
        buff.append(checknorm(int(i)))
    stddist.append(np.std(buff))

plt.plot(n,stddist)
plt.xlabel('Number of samples drawn')
plt.ylabel('Standard deviation')
plt.show()

