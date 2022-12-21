# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define parameters for binomial distribution
n = 10
p = 0.5

# generate binomial distribution
x = np.arange(0, n+1)
y = np.array([])

for i in range(0, n+1):
    y = np.append(y, (np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n-i))) * (p**i) * (1-p)**(n-i))

# plot the graph
plt.plot(x, y, marker="o")
plt.xlabel('Number of Successes')
plt.ylabel('Probability of Successes')
plt.title('Binomial Distribution')
plt.show()
