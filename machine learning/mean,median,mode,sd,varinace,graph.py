import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
incomes=np.random.normal(100,20,10000)
'standard deviation ==middle'
print(np.mean(incomes))
print(np.median(incomes))
print(incomes.std())
print(incomes.var())
plt.hist(incomes,50)
plt.show()
incomes=np.append(incomes,[1000000000])
print(np.mean(incomes))
print(np.median(incomes))
ages=np.random.randint(low=18,high=90,size=500)
#print(ages)
print(stats.mode(ages))

