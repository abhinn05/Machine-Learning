import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gen_random_samples(mu, sigma, n):
    return np.random.normal(mu, sigma, n)

def plot_samples(samples, mu, sigma):
    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=30, density=True, alpha=0.5, color='black', label='Random Samples')
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, norm.pdf(x, mu, sigma), 'r--', label='Parent Distribution')
    plt.title('Random Samples vs Parent Distribution')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

def cal_statistics(samples, mu, sigma):
    mean_sample = np.mean(samples)
    variance_sample = np.var(samples)
    return mean_sample, variance_sample, mu, sigma

def main():
    mu = float(input("Enter the mean of the normal distribution: "))
    sigma = float(input("Enter the standard deviation of the normal distribution: "))
    n_values = [10, 50, 100, 500, 1000]

    for n in n_values:
        print("\nSample Size:", n)
        samples = gen_random_samples(mu, sigma, n)
        plot_samples(samples, mu, sigma)
        mean_sample, variance_sample, parent_mean, parent_std_dev = cal_statistics(samples, mu, sigma)
        print("Sample Mean:", mean_sample)
        print("Sample Variance:", variance_sample)
        print("Parent Mean:", parent_mean)
        print("Parent Standard Deviation:", parent_std_dev)
        print()

if __name__ == "__main__":
    main()
