import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
# uniform distribution
values=np.random.uniform(-10,10,10000)
plt.hist(values,50)
plt.show()

#normal or guassian distribution using pdf
x=np.arange(-3,3,0.001)
plt.plot(x,norm.pdf(x))
plt.show()
# exponential probability distrinbutions

p=np.arange(0,10,.001)
plt.plot(p,expon.pdf(p))
plt.show()
