# In this code, we seek to generate a normal distribution and then sample N values from the distribution
import numpy as np 
import matplotlib.pyplot as plt
# We will define a normal distribution as follows:
# def normal(x,mu,sigma):
#     return ( (1/(2*np.pi*sigma**2) ** -0.5) * np.exp(1/2* -(x-mu)**2/sigma**2))

mu = 0
sigma = 1

x1 = np.random.normal(mu,sigma,1000)
x2 = np.random.normal(mu,sigma,2000)
x3 = np.random.normal(mu,sigma,3000)
x4 = np.random.normal(mu,sigma,4000)

print (f'mean1={np.mean(x1)}')
print (f'mean2={np.mean(x2)}')
print (f'mean3={np.mean(x3)}')
print (f'mean4={np.mean(x4)}')

# print (abs(mu-np.mean(x)) < 0.1)

plt.hist(x1,bins=50, alpha=0.5)
plt.hist(x2,bins=50, alpha=0.5)
plt.hist(x3,bins=50, alpha=0.5)
plt.hist(x4,bins=50, alpha=0.5)

plt.show()

