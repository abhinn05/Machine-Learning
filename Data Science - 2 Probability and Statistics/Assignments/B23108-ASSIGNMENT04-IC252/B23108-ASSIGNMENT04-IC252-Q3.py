import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean_of_A = 78
std_deviation_A = 5
mean_of_B = 85
std_deviation_B = 3
probability_easy = 0.3
probability_medium = 0.5
probability_hard = 0.2

#a
scores = np.linspace(50, 100, 500)
probability_dist_A_easy = probability_easy * norm.pdf(scores, mean_of_A, std_deviation_A)
probability_dist_A_medium = probability_medium * norm.pdf(scores, mean_of_A, std_deviation_A)
probability_dist_A_hard = probability_hard * norm.pdf(scores, mean_of_A, std_deviation_A)

probability_dist_B_easy = probability_easy * norm.pdf(scores, mean_of_B, std_deviation_B)
probability_dist_B_medium = probability_medium * norm.pdf(scores, mean_of_B, std_deviation_B)
probability_dist_B_hard = probability_hard * norm.pdf(scores, mean_of_B, std_deviation_B)

#b
marginal_probability_X_A = probability_dist_A_easy.sum() + probability_dist_A_medium.sum() + probability_dist_A_hard.sum()
marginal_probability_X_B = probability_dist_B_easy.sum() + probability_dist_B_medium.sum() + probability_dist_B_hard.sum()

#c
prob_X_greater_than_80_given_easy = (probability_easy * norm.sf(80, mean_of_A, std_deviation_A)) / probability_easy  # Professor A's exam is used for this calculation

#d
plt.figure(figsize=(10, 6), facecolor='lightgrey')
plt.plot(scores, probability_dist_A_easy, label='Professor A - Easy')
plt.plot(scores, probability_dist_A_medium, label='Professor A - Medium')
plt.plot(scores, probability_dist_A_hard, label='Professor A - Hard')
plt.plot(scores, probability_dist_B_easy, label='Professor B - Easy')
plt.plot(scores, probability_dist_B_medium, label='Professor B - Medium')
plt.plot(scores, probability_dist_B_hard, label='Professor B - Hard')
plt.xlabel('Score', font='Comic Sans MS')
plt.ylabel('Probability Density', font='Comic Sans MS')
plt.title('Probability Density Functions of Professor A and Professor B', font='Comic Sans MS')
plt.legend()
plt.grid(True)
plt.show()

print("Marginal Probability Distribution for Professor A:", marginal_probability_X_A)
print("Marginal Probability Distribution for Professor B:", marginal_probability_X_B)
print("Conditional Probability P(X > 80|Y = 'Easy'):", prob_X_greater_than_80_given_easy)

#e
print("\n(e) Discussion:")
print("If professors were more likely to assign harder exams to students with higher expected scores, the joint probability distribution would change.")