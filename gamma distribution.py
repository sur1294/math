import numpy as np
import matplotlib.pyplot as plt

# Define parameters of Gamma Distribution
alpha = 2.0
beta = 1.0

# Generate 1000 samples from gamma distribution
samples = np.random.gamma(alpha, beta, 1000)

# Plot the histogram
plt.hist(samples, bins=50, density=True)
plt.title("Gamma Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

