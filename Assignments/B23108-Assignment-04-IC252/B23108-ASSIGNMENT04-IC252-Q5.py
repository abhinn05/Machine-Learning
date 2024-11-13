import numpy as np
import matplotlib.pyplot as plt

#a
np.random.seed(42)
X = np.random.uniform(0, 1, 10000)
Y = np.random.uniform(1, 2, 10000)

#b
joint_dist = np.histogram2d(X, Y, bins=20, range=[[0, 1], [1, 2]])[0] / 10000
print("Joint probability distribution:")
print(joint_dist)

#c
X_marginal = np.histogram(X, bins=20, range=(0, 1))[0] / 10000
Y_marginal = np.histogram(Y, bins=20, range=(1, 2))[0] / 10000
independent = np.allclose(joint_dist, np.outer(X_marginal, Y_marginal))
print("Are X and Y independent?", independent)

#d
conditional_probability = np.sum(joint_dist[:, 5:]) / np.sum(joint_dist[:, 5])
print("Conditional probability P(X > 0.5 | Y = 1.5):", conditional_probability)

#e
conditional_dist = joint_dist[:, 5] / np.sum(joint_dist[:, 5])
plt.plot(np.linspace(0, 1, 20), conditional_dist,color='skyblue')
plt.title("Conditional Probability Distribution of X given Y = 1.5", font='Comic Sans MS')
plt.xlabel("X", font='Comic Sans MS')
plt.ylabel("Probability", font='Comic Sans MS')
plt.show()

#f
Z = X + Y

pdf_Z_empirical, bins_Z = np.histogram(Z, bins=20, density=True)
bin_centers_Z = 0.5 * (bins_Z[1:] + bins_Z[:-1])

plt.plot(bin_centers_Z, pdf_Z_empirical, label='Empirical')

pdf_Z_theoretical = np.convolve(X_marginal, Y_marginal, mode='full')[:20]  # Adjusting length

plt.plot(bin_centers_Z, pdf_Z_theoretical, label='Theoretical',color='skyblue')

plt.title("Probability Density Function (pdf) of Z", font='Comic Sans MS')
plt.xlabel("Z", font='Comic Sans MS')
plt.ylabel("Probability Density", font='Comic Sans MS')
plt.legend()
plt.show()


Z_samples = np.random.choice(Z, size=10000, replace=True)
plt.hist(Z_samples, bins=20, density=True, alpha=0.5, label='Empirical',color='skyblue')
plt.plot(bin_centers_Z, pdf_Z_theoretical, color='red', label='Theoretical')
plt.title("Empirical vs Theoretical pdf of Z", font='Comic Sans MS')
plt.xlabel("Z", font='Comic Sans MS')
plt.ylabel("Probability Density", font='Comic Sans MS')
plt.legend()
plt.show()