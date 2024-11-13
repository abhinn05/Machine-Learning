import numpy as np
import matplotlib.pyplot as plt

#a
n = 50
p = [2, 11, 23, 9, 4, 1] 
value_x = np.arange(0, 6)
probability = np.array(p) / n

plt.figure(figsize=(8,4))
plt.subplot(1, 2, 1)
plt.bar(value_x, probability)
plt.title('Probability Density Function (PDF)')
plt.xlabel('Value of Random variable(X)')
plt.ylabel('Probability')

cdf = np.cumsum(probability)
plt.subplot(1, 2, 2)
plt.step(value_x, cdf)
plt.title('Cummulative Distribution Function (CDF)')
plt.xlabel('Value of Random variable(X)')
plt.ylabel('Cummulative Probability')

plt.tight_layout()
plt.show()

#b
ns = [50, 500, 5000]

mean_theory = np.sum(value_x * probability)
theoretical_std_dev = np.sqrt(np.sum(((value_x - mean_theory) ** 2) * probability))
for n in ns:
    x_simu = np.random.choice(value_x, n,p=probability)
    average_X = np.mean(x_simu)

    std_dev = np.std(x_simu)

    print(f"For n={n}:")
    print(f"Simulated average: {average_X}")
    print(f"Simulated standard deviation: {std_dev}")
    print()
    print(f"Theoretical mean: {mean_theory}")
    print(f"Theoretical standard deviation: {theoretical_std_dev}")
    print()

#c
n = 50 
num_experiments = 1000
mean_sample = []

for _ in range(num_experiments):
    x_simu = np.random.choice(value_x, n, p=probability)
    mean_sample.append(np.mean(x_simu)) 


plt.hist(mean_sample, bins=30, alpha=0.7)
plt.title('Histogram of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.show()


print(f"Mean of sample means: {np.mean(mean_sample)}")
print(f"Variance of sample means: {np.var(mean_sample)}")