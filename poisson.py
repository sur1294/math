import matplotlib.pyplot as plt
import numpy as np

# poisson probability distribution
def poisson_distribution(mean,x):
    return (mean**x * np.exp(-mean))/np.math.factorial(x)

# mean
mean = 5
x = np.arange(0,15)

# poisson probability distribution
y = [poisson_distribution(mean,i) for i in x]

# plotting poisson probability distribution
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Poisson Probability Distribution')
plt.show()
