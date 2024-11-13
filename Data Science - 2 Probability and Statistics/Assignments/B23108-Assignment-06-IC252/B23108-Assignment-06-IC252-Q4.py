import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

def gen_random_samples(scale, size):
    return np.random.exponential(scale, size)

def plot_samples(samples, scale):
    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=30, density=True, alpha=0.5, color='black', label='Random Samples')
    x = np.linspace(0, 10*scale, 1000)
    plt.plot(x, expon.pdf(x, scale=scale), 'r--', label='Parent Distribution')
    plt.title('Random Samples vs Parent Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

def calculate_statistics(samples):
    mean_sample = np.mean(samples)
    variance_sample = np.var(samples)
    return mean_sample, variance_sample

def main():
    scale = float(input("Enter the scale parameter of the exponential distribution: "))
    values_size = [10, 50, 100, 500, 1000]

    parent_mean = scale
    parent_variance = scale**2

    print("\nParent Distribution Statistics:")
    print("Parent Mean:", parent_mean)
    print("Parent Variance:", parent_variance)

    for size in values_size:
        print("\nSample Size:", size)
        samples = gen_random_samples(scale, size)
        plot_samples(samples, scale)
        mean_sample, variance_sample = calculate_statistics(samples)
        print("Sample Mean:", mean_sample)
        print("Sample Variance:", variance_sample)
        print()

if __name__ == "__main__":
    main()
