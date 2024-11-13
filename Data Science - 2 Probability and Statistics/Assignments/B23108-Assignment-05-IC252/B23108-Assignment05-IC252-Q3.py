import random
import re
import numpy as np
import matplotlib.pyplot as plt


def sim(n, pF=0.5):
  location_final = []
  for _ in range(10000):
    location = 0
    location += np.random.choice([-1, 1], size=n, p=[1 - pF, pF]).sum()
    location_final.append(location)
  return location_final


#A
n = [100, 1000, 10000]
for i in n:
  plt.subplot(3, 1, n.index(i) + 1)
  location_final = sim(i)
  plt.hist(location_final, bins=40)
  plt.xlabel('Final location')
  plt.ylabel('Frequency')
  plt.title(f'Probability Distribution of Final Locations After {i} Steps')

plt.tight_layout()
plt.show()


#B
n = [100, 1000, 10000]
for i in n:
  plt.subplot(3, 1, n.index(i) + 1)
  location_final = sim(i, 0.6)
  plt.hist(location_final, bins=40)
  plt.xlabel('Final location')
  plt.ylabel('Frequency')
  plt.title(f'Probability Distribution of Final Locations After {i} Steps')

plt.tight_layout()
plt.show()
