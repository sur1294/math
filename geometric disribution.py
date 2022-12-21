import matplotlib.pyplot as plt
import numpy as np

# Geometric Distribution Parameters
p = 0.20

# Calculate Geometric distribution
x = np.arange(1, 11)
geo_dist = p * (1 - p)**(x - 1)

# Plot Geometric Distribution
plt.plot(x, geo_dist, 'o-')
plt.title('Geometric Distribution')
plt.xlabel('Number of trials')
plt.ylabel('Probability of success')
plt.show()

