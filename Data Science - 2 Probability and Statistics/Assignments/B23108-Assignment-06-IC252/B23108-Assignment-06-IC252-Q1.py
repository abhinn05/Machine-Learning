import numpy as np
import scipy.stats
import math
import matplotlib.pyplot as plt

#A

def entropy(prob_head):
    prob_tail = 1 - prob_head
    if prob_head == 0 or prob_tail == 0:
        return 0
    return -(prob_head * math.log2(prob_head) + prob_tail * math.log2(prob_tail))

def entropy_plot():
    probabilities = [i / 100 for i in range(1, 100)]
    entropies = [entropy(p) for p in probabilities]
    plt.plot(probabilities, entropies,color='black')
    plt.xlabel('Probability of Head')
    plt.ylabel('Entropy')
    plt.title('Entropy of a Biased Coin')
    plt.grid(True)
    plt.show()

entropy_plot()

#B

def gaussian_pdf(x, mu, sigma):
    return (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))

def kl_divergence(p_mean, p_var, q_mean, q_var):
    p = scipy.stats.norm(p_mean, np.sqrt(p_var))
    q = scipy.stats.norm(q_mean, np.sqrt(q_var))
    x = np.linspace(min(p_mean - 3 * np.sqrt(p_var), q_mean - 3 * np.sqrt(q_var)),
                    max(p_mean + 3 * np.sqrt(p_var), q_mean + 3 * np.sqrt(q_var)), 1000)
    return scipy.stats.entropy(p.pdf(x), q.pdf(x))

def cross_entropy(p_mean, p_var, q_mean, q_var):
    p = scipy.stats.norm(p_mean, np.sqrt(p_var))
    q = scipy.stats.norm(q_mean, np.sqrt(q_var))
    x = np.linspace(min(p_mean - 3 * np.sqrt(p_var), q_mean - 3 * np.sqrt(q_var)),
                    max(p_mean + 3 * np.sqrt(p_var), q_mean + 3 * np.sqrt(q_var)), 1000)
    return -np.mean(np.log(q.pdf(x)))

def plot_dist(p_mean, p_var, q_mean, q_var):
    p = scipy.stats.norm(p_mean, np.sqrt(p_var))
    q = scipy.stats.norm(q_mean, np.sqrt(q_var))
    x = np.linspace(min(p_mean - 3 * np.sqrt(p_var), q_mean - 3 * np.sqrt(q_var)),
                    max(p_mean + 3 * np.sqrt(p_var), q_mean + 3 * np.sqrt(q_var)), 1000)
    plt.plot(x, p.pdf(x), label='P',color='blue')
    plt.plot(x, q.pdf(x), label='Q',color='green')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.title('Gaussian Distributions')
    plt.show()

def experiment(p_mean, p_var, q_mean, q_var):
    plot_dist(p_mean, p_var, q_mean, q_var)
    kl_div = kl_divergence(p_mean, p_var, q_mean, q_var)
    cross_ent = cross_entropy(p_mean, p_var, q_mean, q_var)
    print(f"KL Divergence: {kl_div}")
    print(f"Cross-Entropy: {cross_ent}\n")

print("Experiment 1: Overlapping Distributions")
experiment(0, 1, 0, 1)

print("Experiment 2: Partially Overlapping Distributions")
experiment(0, 1, 2, 1)

print("Experiment 3: Non-Overlapping Distributions")
experiment(0, 1, 5, 1)
