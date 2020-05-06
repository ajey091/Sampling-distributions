from scipy.stats import bernoulli
import scipy
import numpy as np 
import matplotlib.pyplot as plt 

p = 0.3
rv = bernoulli(p) # Initiating a Bernoulli process with a probability p
moe = []
# n samples from the distribution
nvals = np.linspace(20,1000,10)
for n in nvals:
    # sample = rv.rvs(int(n))
    # n1 = sum(sample == 0)
    # n2 = n - n1
    # x = np.linspace(0,1,100)
    # L = x**n2 * (1-x)**n1

    max_x = []
    for iter in range(1000):
        sample = rv.rvs(int(n))
        n1 = sum(sample == 0)
        n2 = n - n1
        x = np.linspace(0,1,100)
        L = x**n2 * (1-x)**n1
        curr_max_x = scipy.optimize.fmin(lambda x: -(x**n2 * (1-x)**n1), 0, disp=False)
        max_x.append(curr_max_x[0])

    max_x_mean = np.mean(max_x)
    std_err = np.std(max_x)/(n)**0.5
    conf_int = np.percentile(max_x, [2.5,97.5])

    z = scipy.stats.norm.ppf(1-(1-0.95)/2)
    moe.append(z*std_err)

plt.plot(nvals,moe)
plt.xlabel('Sample size')
plt.ylabel('Margin of error')
plt.show()



