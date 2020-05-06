import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('advertising.csv')
print (data.head())
plt.plot(data.iloc[:,0], data.iloc[:,3],'*')
plt.show()


