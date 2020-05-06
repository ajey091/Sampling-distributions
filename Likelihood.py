from scipy.stats import bernoulli
import scipy
import numpy as np 
import matplotlib.pyplot as plt 

p = 0.3
rv = bernoulli(p) # Initiating a Bernoulli process with a probability p

# n samples from the distribution

n = 100
sample = rv.rvs(n)
print (sample)
n1 = sum(sample == 0)
n2 = n - n1
x = np.linspace(0,1,100)
L = x**n2 * (1-x)**n1

# plt.plot(x,L)
# plt.ylabel('Likelihood function')
# plt.xlabel(r"$\Theta$")
# plt.show()


max_x = scipy.optimize.fmin(lambda x: -(x**n2 * (1-x)**n1), 0)
# print (f'The likelihood function is maximum at {max_x}')


max_x = []
for iter in range(1000):
    sample = rv.rvs(n)
    n1 = sum(sample == 0)
    n2 = n - n1
    x = np.linspace(0,1,100)
    L = x**n2 * (1-x)**n1
    curr_max_x = scipy.optimize.fmin(lambda x: -(x**n2 * (1-x)**n1), 0, disp=False)
    max_x.append(curr_max_x[0])

# plt.hist(max_x, bins=10)
# plt.xlabel(r"$\Theta$")
# plt.ylabel('Frequency')
# plt.show()

max_x_mean = np.mean(max_x)
std_err = np.std(max_x)/(n)**0.5
conf_int = np.percentile(max_x, [2.5,97.5])

print (f'mean of theta = {max_x_mean:.4f}')
print (f'Standard error of theta = {std_err:.4f}')
print (f'95% Confidence interval of theta = {conf_int}')

z = scipy.stats.norm.ppf(1-(1-0.95)/2)
print(f'Z-score for 95% confidence interval = {z:0.3f}')
moe = z*std_err
print (f'Margin of error={moe:.3f}')

# print (f'Maximum value of p={max_x}')
# plt.plot(x,L)
# plt.xlabel('Theta')
# plt.ylabel('Likelihood')
# plt.show()


# x = np.linspace(0.0001,0.999,100)
# LogL = n2*np.log(x) + (n1)*np.log(1-x)
# max_x = scipy.optimize.fmin(lambda x: -(n2*np.log(x) + (n1)*np.log(1-x)), 0)
# print (f'The likelihood function is maximum at {max_x}')
# plt.plot(x,LogL)
# plt.xlabel(r"$\Theta$")
# plt.ylabel('Log Likelihood function')
# plt.show()



