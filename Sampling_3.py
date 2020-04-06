import scipy.stats
import numpy as np 
import matplotlib.pyplot as plt 

weight = scipy.stats.lognorm(0.23, 0, 70.8)
print (f'{weight.mean():.2f}, {weight.std():.2f}')

xs = np.linspace(20,160,100)
ys = weight.pdf(xs)

# plt.plot(xs,ys)
# plt.xlabel('Weight (kg)')
# plt.show()

# Draw sample
# The goal is to get an estimate of the means by sampling 100 items from the distribution repeated 1000 times

def calc_stats(n):
    samplestat = []
    for _ in range(n):
        samplestat.append(np.median(weight.rvs(100)))

    samp_stat_mean = np.mean(samplestat)
    # print (f'Mean of the sample means={samp_mean:.2f}')

    std_err = np.std(samplestat)
    # print(f'Standard error={std_err:.2f}')

    conf_int = np.percentile(samplestat, [5,95])
    # print (f'95% Confidence interval = {conf_int}')

    return samp_stat_mean,std_err,conf_int


print (calc_stats(1000))
