import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(1,21,1)
e = np.e
y=[]
for n in t:
    pi = np.pi
    j = (math.factorial(n))/(((2*pi*n)**(1/2))*((n/e)**n))
    y.append(j)
plt.plot(t,y,color="purple")
plt.xlabel("Number")
plt.ylabel("Ratio")
plt.show()
