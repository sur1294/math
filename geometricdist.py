import numpy as np
import matplotlib.pyplot as plt

def geometric_distribution(p, n):
    x = [0]
    for i in range(1, n+1):
        x.append(x[i-1] + p*(1-p)**(i-1))
    return x

probability = 0.2
n = 10

x = geometric_distribution(probability, n)

plt.plot(x)
plt.xlabel('n')
plt.ylabel('Probability of Success')
plt.title('Geometric Distribution')
plt.show()
