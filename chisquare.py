import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

# Creating a chi-squared distribution
chi_squared_dist = st.chi2(5)

# Generating random variates
random_variates = chi_squared_dist.rvs(1000)

# Plotting the histogram
plt.hist(random_variates, bins=20, density=True)

# Plotting the probability density function
x = np.linspace(0, 20, 1000)
y = chi_squared_dist.pdf(x)
plt.plot(x, y, 'r-', lw=2, alpha=0.6)

plt.title("Chi-squared Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density Function")

plt.show()

