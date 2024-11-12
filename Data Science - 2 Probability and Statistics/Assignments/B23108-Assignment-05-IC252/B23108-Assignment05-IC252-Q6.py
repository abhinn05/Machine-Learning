import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

f = lambda x: np.sin(3*x)**4

fig, h = plt.subplots(ncols=2, figsize=(10, 5))
x = np.linspace(0, np.pi, 100)
y = f(x)
h[0].plot(x, y)

integral_act = quad(f, 0, np.pi)[0]
h[1].axhline(y=integral_act, color='black', linestyle='-')

N = 2000

count = 0
for i in range(N):
    x = np.random.rand()*np.pi
    y = np.random.rand()
    if y < f(x):
        count += 1

    h[0].plot(x, y, 'ro', markersize=2)
    h[1].plot(i, np.pi*count/(i+1), 'ro', markersize=2,color='purple')
    plt.pause(0.01)

plt.show()
    
integral = np.pi*count/N

print(f'Integral value from Simulation: {integral:.4f}')
print(f'Actual Integral Value: {integral_act:.4f}')
