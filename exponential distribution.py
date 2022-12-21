import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# generate exponential distribution
x = np.arange(0, 10, 0.001)
y = stats.expon.pdf(x)

# plot exponential distribution
plt.plot(x, y)
plt.title('Exponential Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.show()
