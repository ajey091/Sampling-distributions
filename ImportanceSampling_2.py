import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats

f_x = scipy.stats.randint(1,7)

def g_x(x):
    return (7-x)/10/2.1

E_g = np.dot(np.linspace(1,6,6),g_x(np.linspace(1,6,6)))
print (E_g)

plt.bar(np.linspace(1,6,6),g_x(np.linspace(1,6,6)))
plt.ylabel('pdf of biased die')
# plt.savefig('BiasedDie_pdf.png')
plt.show()

plt.bar(np.linspace(1,6,6),[1/6]*6,color='red')
plt.ylabel('pdf of fair die')
# plt.savefig('FairDie_pdf.png')
plt.show()

E_f_approx = []
E_g_approx = []
for iter in range(5000):
    fval = f_x.rvs(1)
    fval = fval[0]
    E_f_approx.append(fval)
    w = g_x(fval)/(1/6)
    E_g_approx.append(fval * w)
    plt.plot(iter,np.mean(E_f_approx),'r.')
    plt.plot(iter,np.mean(E_g_approx),'b.')

plt.plot(iter,np.mean(E_f_approx),'r.',label='Fair die')
plt.plot(iter,np.mean(E_g_approx),'b.',label='Biased die')
plt.xlabel('Iterations')
plt.ylabel('Expected value')
plt.axhline(y=3.5, color='r', linestyle='-',label='Fair die (Truth)')
plt.axhline(y=E_g, color='b', linestyle='-',label='Biased die (Truth)')
plt.legend(loc='best')
plt.savefig('Importance_Sampling_dice.png')

print (np.mean(E_f_approx))
print (np.mean(E_g_approx))
