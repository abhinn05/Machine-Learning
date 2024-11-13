import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon

#A

np.random.seed(42)
data_uniform = np.random.uniform(0, 1, 1000)
data_normal = np.random.normal(0, 1, 1000)

def exp_truncated(a, b, size):
    lambda_val = 1.0 / (b - a)
    u = np.random.uniform(0, 1, size)
    return -np.log(1 - u*(1 - np.exp(-lambda_val*(b - a)))) / lambda_val + a

truncated_exp_data = exp_truncated(0, 5, 1000)  

fig, axes = plt.subplots(3, 1, figsize=(8, 12))

axes[0].hist(data_uniform, bins=30, density=True, alpha=0.5, color='purple', label='Sample Data')
x = np.linspace(0, 1, 100)
axes[0].plot(x, np.ones_like(x), 'r--', label='Density Function')
axes[0].set_title('Uniform Distribution')
axes[0].legend()

axes[1].hist(data_normal, bins=30, density=True, alpha=0.5, color='yellow', label='Sample Data')
x = np.linspace(-4, 4, 100)
axes[1].plot(x, norm.pdf(x, 0, 1), 'r--', label='Density Function')
axes[1].set_title('Normal Distribution')
axes[1].legend()

axes[2].hist(truncated_exp_data, bins=30, density=True, alpha=0.5, color='orange', label='Sample Data')
x = np.linspace(0, 5, 100)
axes[2].plot(x, expon.pdf(x, 0, 1/5), 'r--', label='Density Function')
axes[2].set_title('Truncated Exponential Distribution')
axes[2].legend()

plt.tight_layout()
plt.show()

#B
import numpy as np
import matplotlib.pyplot as plt

def density_function(x):
    return (1/40) * (2*x + 3)

def inverse_cdf(u):
    return (40 * np.sqrt(u * 10 + 3) - 3) / 2

def generate_random_samples(size):
    u = np.random.uniform(0, 1, size)
    return inverse_cdf(u)

random_samples = generate_random_samples(1000)

x = np.linspace(0, 5, 100)
plt.plot(x, density_function(x), label='Density Function', color='black')

plt.hist(random_samples, bins=30, density=True, alpha=0.5, color='green', label='Sample Data')

plt.title('Density Function and Histogram of Random Draws')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
