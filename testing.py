import numpy as np
import random

quar_popsize = 4
num_params = 10
bestOnes = np.ones([4,10])
def crossover():
    output = np.zeros([quar_popsize, num_params])
    a = bestOnes[random.randrange(quar_popsize)]
    b = bestOnes[random.randrange(quar_popsize)]

    for i in range(quar_popsize):
      mask1 = np.random.binomial(1, .50, size=num_params)
      mask2 = (mask1 - np.ones(num_params)) * -1
      output[i] = (a * mask1) + (b * mask2)
    return output

print(crossover())