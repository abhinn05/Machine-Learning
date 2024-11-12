import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
samples_number = 1000000
weather_conditions = ['Sunny', 'Rainy', 'Cloudy']
choices_clothing = ['T-shirt', 'Sweater', 'Jacket']
sample_weather = np.random.choice(weather_conditions, samples_number)
samples_cloth = np.random.choice(choices_clothing, samples_number)

data = {'Weather': sample_weather, 'Clothing': samples_cloth}
df = pd.DataFrame(data)
joint_probability_table = pd.crosstab(df['Weather'], df['Clothing'], normalize=True)

marginal_weather = df['Weather'].value_counts(normalize=True)
marginal_clothing = df['Clothing'].value_counts(normalize=True)

plt.figure(figsize=(10, 5), facecolor='lightblue')
plt.subplot(1, 2, 1)
marginal_weather.plot(kind='bar', color='skyblue')
plt.title('Marginal Probability of Weather', font = 'Comic Sans MS')
plt.xlabel('Weather Condition', font = 'Comic Sans MS')
plt.ylabel('Probability', font = 'Comic Sans MS')

plt.subplot(1, 2, 2)
marginal_clothing.plot(kind='bar', color='pink')
plt.title('Marginal Probability of Clothing Choice', font = 'Comic Sans MS')
plt.xlabel('Clothing Choice', font = 'Comic Sans MS')
plt.ylabel('Probability', font = 'Comic Sans MS')

plt.tight_layout()
plt.show()

conditional_probability_table = joint_probability_table.div(marginal_weather, axis=0)

print("Joint Probability Table:")
print(joint_probability_table)
print("\nConditional Probability of Clothing Choice given Weather Condition:")
print(conditional_probability_table)