import numpy as np 
import scipy.stats

for n in np.linspace(1,100,5):
    dist1 = scipy.stats.norm(0.0,1.0)
    dist2 = scipy.stats.norm(0.0,1.0)
    samp1 = dist1.rvs(n)
    samp2 = dist2.rvs(n)
    # res1 = scipy.stats.kstest(samp1,'norm')
    # res2 = scipy.stats.kstest(samp2,'norm')
    # print (f'pvalue for 1:{res1[1]}')
    # print (f'pvalue for 2:{res2[1]}')
