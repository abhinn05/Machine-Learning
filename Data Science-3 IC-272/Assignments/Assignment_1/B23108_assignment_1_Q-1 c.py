import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("landslide_data_original.csv")

filtered_data = df[df['stationid'] == 't12']['humidity'].dropna()

bin_size = 5
min_humidity = filtered_data.min()
max_humidity = filtered_data.max()

bin_edges = list(range(int(min_humidity) - (int(min_humidity) % bin_size), int(max_humidity) + bin_size, bin_size))

histogram = [0] * (len(bin_edges) - 1)
for value in filtered_data:
    for i in range(len(bin_edges) - 1):
        if bin_edges[i] <= value < bin_edges[i + 1]:
            histogram[i] += 1
            break

plt.bar(bin_edges[:-1], histogram, width=bin_size, edgecolor='black', align='edge')
plt.title('Histogram of Humidity for Station ID t12')
plt.xlabel('Humidity')
plt.ylabel('Frequency')
plt.xticks(bin_edges)  
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
