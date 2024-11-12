import numpy as np
import matplotlib.pyplot as plt

probability_defective_incandescent = 0.1
probability_defective_led = 0.05

num_incandescent_bulbs = 2
num_led_bulbs = 3

#a
joint_dist = np.zeros((num_incandescent_bulbs + 1, num_led_bulbs + 1))
for i in range(num_incandescent_bulbs + 1):
    for j in range(num_led_bulbs + 1):
        joint_dist[i, j] = (np.math.comb(num_incandescent_bulbs, i) * (probability_defective_incandescent ** i) *
                                    np.math.comb(num_led_bulbs, j) * (probability_defective_led ** j))
joint_dist /= np.sum(joint_dist)

plt.imshow(joint_dist, cmap='Greens')
plt.colorbar(label='Probability')
plt.xlabel('Number of Defective LED Bulbs (Y)')
plt.ylabel('Number of Defective Incandescent Bulbs (X)')
plt.xticks(range(num_led_bulbs + 1))
plt.yticks(range(num_incandescent_bulbs + 1))
plt.title('Joint Distribution')
plt.show()

#b
X_marginal = np.sum(joint_dist, axis=1)
Y_marginal = np.sum(joint_dist, axis=0)

print("\nMarginal Distribution of X (Defective Incandescent Bulbs):", X_marginal)
print("Marginal Distribution of Y (Defective LED Bulbs):", Y_marginal)

#c
plt.bar(range(len(X_marginal)), X_marginal, color='green')
plt.xlabel('Number of Defective Incandescent Bulbs (X)')
plt.ylabel('Probability')
plt.title('PMF of X')
plt.xticks(range(len(X_marginal)))
plt.show()

#d
conditional_prob = (num_incandescent_bulbs - 1) * probability_defective_incandescent / num_incandescent_bulbs
print("\nConditional Probability of Getting One Defective Bulb given First Chosen is Incandescent:", conditional_prob)

#e
print("\nX and Y are not independent events because the probability of one event depends on the outcome of the other.")

#f
print("\nIf bulbs were drawn with replacement, the joint probability distribution would change because the probabilities would remain constant for each pick.")

#g
print("\nIf sampling with replacement, the probabilities would remain the same because the probabilities of each outcome would not change.")