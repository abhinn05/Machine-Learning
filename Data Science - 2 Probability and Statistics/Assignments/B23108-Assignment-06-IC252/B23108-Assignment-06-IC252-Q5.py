import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#A

mean_population = 65
std_population = 15

size_sample = 50    
num_sample = 5
sample_random = np.random.normal(mean_population, std_population, (num_sample, size_sample))

mean_sample = np.mean(sample_random, axis=1)
stds_sample = np.std(sample_random, axis=1)

plt.figure(figsize=(10, 6))

x = np.linspace(0, 130, 1000)
plt.plot(x, norm.pdf(x, mean_population, std_population), 'r--', label='Population')

for i in range(num_sample):
    plt.hist(sample_random[i], bins=30, density=True, alpha=0.5, label=f'Sample {i+1}',color='green')

plt.title('Histogram of Random Samples and Population')
plt.xlabel('Marks')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

for i in range(num_sample):
    print(f"Sample {i+1}: Mean = {mean_sample[i]}, Standard Deviation = {stds_sample[i]}")


#B

size_sample = [100, 150, 250]
num_sample = 5
random_size_sample = {}

for size in size_sample:
    random_size_sample[size] = np.random.normal(mean_population, std_population, (num_sample, size))

plt.figure(figsize=(12, 8))

x = np.linspace(0, 130, 1000)
plt.plot(x, norm.pdf(x, mean_population, std_population), 'r--', label='Population')

for size in size_sample:
    for i in range(num_sample):
        plt.hist(random_size_sample[size][i], bins=30, density=True, alpha=0.5, label=f'Size {size}',color='blue')

plt.title('Histogram of Random Samples with Different Sizes and Population')
plt.xlabel('Marks')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

for size in size_sample:
    mean_sample = np.mean(random_size_sample[size], axis=1)
    stds_sample = np.std(random_size_sample[size], axis=1)
    print(f"Sample Size {size}: Mean = {np.mean(mean_sample)}, Standard Deviation = {np.mean(stds_sample)}")

#C
    
def systematic_sampling(population, sample_size):
    k = len(population) // sample_size
    indices = np.arange(0, len(population), k)
    return population[indices]

systematic_sample_size = {}
for size in size_sample:
    systematic_sample_size[size] = np.array([systematic_sampling(random_size_sample[size][0], size) for _ in range(num_sample)])

plt.figure(figsize=(12, 8))

x = np.linspace(0, 130, 1000)
plt.plot(x, norm.pdf(x, mean_population, std_population), 'r--', label='Population')

for size in size_sample:
    for i in range(num_sample):
        plt.hist(systematic_sample_size[size][i], bins=30, density=True, alpha=0.5, label=f'Systematic Size {size}',color='black')

plt.title('Histogram of Systematic Samples with Different Sizes and Population')
plt.xlabel('Marks')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

for size in size_sample:
    mean_sample = np.mean(systematic_sample_size[size], axis=1)
    stds_sample = np.std(systematic_sample_size[size], axis=1)
    print(f"Systematic Sample Size {size}: Mean = {np.mean(mean_sample)}, Standard Deviation = {np.mean(stds_sample)}")


#D
    
print("\nComparison of Statistics:")

for size in size_sample:
    print(f"Sample Size {size}:")
    
    random_means = np.mean(random_size_sample[size], axis=1)
    random_stds = np.std(random_size_sample[size], axis=1)
    random_mean_bias = np.mean(random_means) - mean_population
    random_std_bias = np.mean(random_stds) - std_population
    random_mean_variance = np.var(random_means)
    random_std_variance = np.var(random_stds)
    
    print("Random Sampling:")
    print(f"  Mean Bias: {random_mean_bias}, Standard Deviation Bias: {random_std_bias}")
    print(f"  Mean Variance: {random_mean_variance}, Standard Deviation Variance: {random_std_variance}")
    
    systematic_means = np.mean(systematic_sample_size[size], axis=1)
    systematic_stds = np.std(systematic_sample_size[size], axis=1)
    systematic_mean_bias = np.mean(systematic_means) - mean_population
    systematic_std_bias = np.mean(systematic_stds) - std_population
    systematic_mean_variance = np.var(systematic_means)
    systematic_std_variance = np.var(systematic_stds)
    
    print("Systematic Sampling:")
    print(f"  Mean Bias: {systematic_mean_bias}, Standard Deviation Bias: {systematic_std_bias}")
    print(f"  Mean Variance: {systematic_mean_variance}, Standard Deviation Variance: {systematic_std_variance}")
    print()
