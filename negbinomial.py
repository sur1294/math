import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nbinom

# Parameters
n = 3 # Number of trials
p = 0.2 # Probability of success

# Calculate Mean and Variance
mean = n * p 
var = n * p * (1 - p)

# Generate the random variables
x = np.arange(0, 8)

# Calculate PMF
prob = nbinom.pmf(x, n, p)

# Plot
plt.plot(x, prob, 'o-')
plt.title('Negative Binomial: n = %i , p = %.2f' % (n, p), fontsize=15)
plt.xlabel('Number of Successes', fontsize=15)
plt.ylabel('Probability of Successes', fontsize=15)
plt.show()
