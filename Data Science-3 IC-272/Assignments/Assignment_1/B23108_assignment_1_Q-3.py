import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

original_data = pd.read_csv('landslide_data_original.csv')
missing_data = pd.read_csv('landslide_data_miss.csv')

def linear_interp(dataframe):
    for col in dataframe.columns:
        if dataframe[col].isnull().any(): 
            dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce')
            for idx in range(len(dataframe)):
                if pd.isnull(dataframe.loc[idx, col]):
                    prev_idx = dataframe.iloc[:idx][col].last_valid_index()
                    next_idx = dataframe.iloc[idx:][col].first_valid_index()
                    
                    if prev_idx is not None and next_idx is not None:
                        prev_val = dataframe.loc[prev_idx, col]
                        next_val = dataframe.loc[next_idx, col]
                        dataframe.loc[idx, col] = prev_val + (next_val - prev_val) * (idx - prev_idx) / (next_idx - prev_idx)
    return dataframe

interpolated_data = linear_interp(missing_data)

plt.title('Boxplot of Attributes')
interpolated_data.boxplot()
plt.tight_layout()
plt.show()

def find_outliers(dataframe):
    outlier_indices = {}
    for col in dataframe.columns:
        if dataframe[col].dtype in [float, int]:  
            vals = dataframe[col].dropna()
            first_quartile = vals.quantile(0.25)
            third_quartile = vals.quantile(0.75)
            interquartile_range = third_quartile - first_quartile
            lower_limit = first_quartile - 1.5 * interquartile_range
            upper_limit = third_quartile + 1.5 * interquartile_range
            outlier_indices[col] = vals[(vals < lower_limit) | (vals > upper_limit)].index.tolist()
    return outlier_indices

outliers_dict = find_outliers(interpolated_data)
print("Detected outliers:", outliers_dict)

def calc_median(vals):
    sorted_vals = sorted(vals)
    n = len(sorted_vals)
    if n == 0:
        return np.nan
    if n % 2 == 1:
        return sorted_vals[n // 2]
    else:
        mid1 = sorted_vals[n // 2 - 1]
        mid2 = sorted_vals[n // 2]
        return (mid1 + mid2) / 2

def replace_outliers(dataframe, outliers):
    for col, idx_list in outliers.items():
        if dataframe[col].dtype in [float, int]:
            col_vals = dataframe[col].dropna()
            col_median = calc_median(col_vals)
            dataframe.loc[idx_list, col] = col_median
    return dataframe

cleaned_data = replace_outliers(interpolated_data.copy(), outliers_dict)
plt.title('Boxplot After Replacing Outliers with Median')
cleaned_data.boxplot()
plt.tight_layout()
plt.show()
