# ok so a quick note
#so there are varius kind of probability distributions in practical world
#distributions can be based on continues or discreate data
#when we have discreate data we apply pmf(probability density function )
#when we have continous data we apply pdf(probability density function)
#and i seriously dont know why
#here is the code to get things done in python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson#ss
# uniform distribution
values=np.random.uniform(-10,10,10000)
plt.hist(values,50)
plt.show()

#normal or guassian distribution using pdf
x=np.arange(-3,3,0.001)
plt.plot(x,norm.pdf(x))
plt.show()
# exponential probability distrinbutions(decreasing)

p=np.arange(0,10,.001)
plt.plot(p,expon.pdf(p))
plt.show()

#binomial distribtution
n,m=10,0.5
plt.plot(p,binom.pmf(p,n,m))
plt.show()
#poisson distribution (u know predict the future thing(google it))
mu = 500
x = np.arange(400, 600,0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()
