import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def Pi_estimate(n):
  l = 0
  for i in range(n):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
      l += 1
  estimatedPi = 4 * l / n
  return estimatedPi


n = 3000

print(f'Estimate of Pi for {n} Samples: {Pi_estimate(n)}')


def update(n):
  global estimates
  estimates.append(Pi_estimate(n + 1))
  ax.clear()
  ax.plot(np.arange(len(estimates)), estimates)
  ax.axhline(y=np.pi, color='b', linestyle='--')
  ax.set_xlabel('Number of Samples')
  ax.set_ylabel('Estimate of pi')
  ax.set_title('Monte Carlo Estimation of pi')


estimates = []
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=3000, interval=5)
plt.show()
