import numpy as np 
import scipy.stats
import matplotlib.pyplot as plt

# Comparison of heights of males and females
# The (mean, std) of men and women are (178, 7.7) and (163, 7.3)

mu_men, sigma_men = 178, 7.7
mu_women, sigma_women = 163, 7.3

men = scipy.stats.norm(mu_men, sigma_men)
women = scipy.stats.norm(mu_women, sigma_women)

def eval_pdf(rv, num=4):
    mean, std = rv.mean(), rv.std()
    xs = np.linspace(mean - num*std, mean + num*std, 100)
    ys = rv.pdf(xs)
    return xs, ys


x_men, y_men = eval_pdf(men)
x_women, y_women = eval_pdf(women)

plt.plot(x_men, y_men, label='Men height distribution')
plt.plot(x_women, y_women, label='Women height distribution')
plt.legend(loc='best')
plt.xlabel('Height in cm')
plt.show()

men_samples = men.rvs(1000)
women_samples = women.rvs(1000)
plt.hist(men_samples, alpha = 0.5)
plt.hist(women_samples, alpha = 0.5)
plt.xlabel('Height in cm')
plt.show()