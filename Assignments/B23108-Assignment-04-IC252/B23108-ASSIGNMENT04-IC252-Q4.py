import numpy as np
import matplotlib.pyplot as plt

mean_AM = 1
std_deviation_AM = 0.5
mean_FM = 1.5
std_dev_FM = 0.75

repair_times_AM = np.random.normal(mean_AM, std_deviation_AM, 100)
repair_times_FM = np.random.normal(mean_FM, std_dev_FM, 100)

plt.figure(figsize=(8, 6), facecolor='lightgrey')
plt.scatter(repair_times_AM, repair_times_FM, color='lightblue', label='Repair Times')
plt.xlabel('Repair Time for AM Radios (hours)', font='Comic Sans MS')
plt.ylabel('Repair Time for FM Radios (hours)', font='Comic Sans MS')
plt.title('Joint Probability Distribution of Repair Times', font='Comic Sans MS')
plt.legend()
plt.grid(True)
plt.show()

number_simulations = 100000
am_2_hours = np.random.normal(mean_AM, std_deviation_AM, number_simulations)
fm_less_than_1_hour = np.random.normal(mean_FM, std_dev_FM, number_simulations) < 1

prob_less_than_1_hour = np.mean(fm_less_than_1_hour[am_2_hours >= 2])

print("Probability that the repair time for the FM radio will be less than 1 hour given the AM radio repair takes 2 hours:", prob_less_than_1_hour)

total_repair_times = repair_times_AM + repair_times_FM

plt.figure(figsize=(8, 6), facecolor='lightgrey')
plt.hist(total_repair_times, bins=20, color='skyblue', alpha=0.7, density=True)
plt.xlabel('Total Repair Time (hours)', font='Comic Sans MS')
plt.ylabel('Probability Density', font='Comic Sans MS')
plt.title('Distribution of Total Repair Time', font='Comic Sans MS')
plt.grid(True)
plt.show()

mean_total_repair_time = np.mean(total_repair_times)
std_deviation_total_repair_time = np.std(total_repair_times)

print("Mean of Total Repair Time:", mean_total_repair_time)
print("Standard Deviation of Total Repair Time:", std_deviation_total_repair_time)