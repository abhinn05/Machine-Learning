import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("landslide_data_miss.csv")
df = df.dropna(subset=['stationid'])
threshold = len(df.columns) / 3  
df = df.dropna(thresh=len(df.columns) - threshold)

mean_temp = df['temperature'].mean()
print("Original Mean of temperature = ", mean_temp)

column_data = sorted(df['temperature'].dropna().tolist())
n = len(column_data)
median_temp = (column_data[n//2] + column_data[(n//2) - 1])/2 if n % 2 == 0 else column_data[n//2]
print("Original Median of Temperature = ", median_temp)

def std(mean, data):
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return std_dev

std_temp = std(mean_temp, df['temperature'].dropna().tolist())
print("Original Standard Deviation of Temperature = ", std_temp)

def linear_interpolate(column):
    col_array = column.to_numpy()
    missing_indices = np.isnan(col_array)
    
    for i in range(len(col_array)):
        if missing_indices[i]:
            prev_idx = i - 1
            while prev_idx >= 0 and missing_indices[prev_idx]:
                prev_idx -= 1
            
            next_idx = i + 1
            while next_idx < len(col_array) and missing_indices[next_idx]:
                next_idx += 1
            
            if prev_idx >= 0 and next_idx < len(col_array):
                prev_value = col_array[prev_idx]
                next_value = col_array[next_idx]
                col_array[i] = prev_value + (next_value - prev_value) * (i - prev_idx) / (next_idx - prev_idx)
    
    return pd.Series(col_array, index=column.index)

for column in df.columns:
    if df[column].dtype in [np.float64, np.int64]:  
        df[column] = linear_interpolate(df[column])

original_df = pd.read_csv("D:\\College\\Sem 3\\Machine Learning\\2024\\Assignments\\1\\landslide_data_original.csv")
interpolated_df = df

# Select only numeric columns for RMSE calculation
numeric_cols = original_df.select_dtypes(include=[np.number]).columns
original_df_numeric = original_df[numeric_cols]
interpolated_df_numeric = interpolated_df[numeric_cols]

def compute_rmse(original_df, interpolated_df):
    rmse_dict = {}
    
    for column in original_df.columns:
        original_values = original_df[column].dropna()
        interpolated_values = interpolated_df[column].dropna()
        
        aligned_values = pd.DataFrame({'original': original_values, 'interpolated': interpolated_values})
        mse = ((aligned_values['original'] - aligned_values['interpolated']) ** 2).mean()
        rmse = mse ** 0.5
        rmse_dict[column] = rmse
    
    return rmse_dict

rmse_values = compute_rmse(original_df_numeric, interpolated_df_numeric)
attributes = list(rmse_values.keys())
rmse = list(rmse_values.values())

plt.bar(attributes, rmse, edgecolor='black')
plt.xlabel('Attributes')
plt.ylabel('RMSE')
plt.title('RMSE of Interpolated Values vs Original Values')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
