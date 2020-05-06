import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats
from random import  uniform

p = scipy.stats.norm(0,1)

n = 50000
int_val = [0]*n
mean_val = [0]*n

for iter in range(n):
    x = uniform(4, 100)
    w = 1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2+x-4)
    q = np.exp(4-x)
    int_val[iter] = q*w
    mean_val[iter] = sum(int_val)/(iter+1)
    

plt.plot(np.linspace(1,n,n),mean_val,'r.')
plt.xlabel('Iterations')
plt.ylabel('Estimated probability')
plt.savefig('ImportanceSampling_3.png')

print (f'The estimated probability of Z>4 = {np.mean(int_val):0.3e}')
print (f'The standard error of the estimate = {np.std(int_val):0.3e}')
