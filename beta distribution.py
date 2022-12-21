import matplotlib.pyplot as plt 
import numpy as np 
from scipy.stats import beta 

#Setting parameters
alpha = 0.5
beta = 0.5

#Generating data
x = np.linspace(0,1,200) 
y = beta.pdf(x, alpha, beta) 

#Plotting the graph
plt.plot(x,y) 
plt.xlabel('x') 
plt.ylabel('Probability Density') 
plt.title('Beta Distribution') 
plt.show()
