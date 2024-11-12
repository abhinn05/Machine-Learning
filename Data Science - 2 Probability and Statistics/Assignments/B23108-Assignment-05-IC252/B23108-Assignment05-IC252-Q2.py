import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#A
prob_dict = {'Grocery/Pharmacy': 0.2, 'Parks': 0.02, 'Residential': 0.5, 'Retail': 0.2, 'Workplace': 0.03, 'Transport': 0.05}
df = pd.read_csv('C:/Users/Abhinn/Desktop/B23108-Assignment-05-IC252/2021_IN_Region_Mobility_Report.csv')
mumbai_suburban = df[df['sub_region_2'] == 'Mumbai Suburban'].iloc[:, -7:]
mumbai_suburban.columns = ['Date', 'Retail', 'Grocery/Pharma', 'Parks', 'Transport', 'Workplace', 'Residential']
mumbai_suburban['Date'] = pd.to_datetime(mumbai_suburban['Date'])

change_mean = mumbai_suburban.iloc[:, 1:].mean()

#B
subset = mumbai_suburban[(mumbai_suburban['Date'] >= '2021-04-01') & (mumbai_suburban['Date'] <= '2021-05-20')].copy()
subset['Expected'] = subset['Retail']*prob_dict['Retail'] + subset['Grocery/Pharma']*prob_dict['Grocery/Pharmacy'] + subset['Parks']*prob_dict['Parks'] + subset['Transport']*prob_dict['Transport'] + subset['Workplace']*prob_dict['Workplace'] + subset['Residential']*prob_dict['Residential']

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
subset.plot(kind='line', x='Date', color = colors)
plt.title('Mobility Trends in Mumbai Suburban')
plt.ylabel('Mobility Trends')
plt.xlabel('Date')
plt.show()


subset.iloc[:,1:].mean().plot(kind='bar', color = colors)
plt.title('Average Mobility Trends in Mumbai Suburban')
plt.ylabel('Mobility Trends')
plt.xlabel('Category')
plt.show()


rms_error = ((subset['Expected'] - subset['Retail'])**2).mean()**0.5
mae = (subset['Expected'] - subset['Retail']).abs().mean()
kl_divergence = (subset['Expected']*np.log(subset['Expected']/subset['Retail'])).sum()

print(f'RMS Error: {rms_error:.3f}\nMAE: {mae:.3f}\nKL Divergence: {kl_divergence:.3f}')