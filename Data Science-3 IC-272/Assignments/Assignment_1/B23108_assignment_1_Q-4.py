import pandas as pd
import numpy as np

data_with_gaps = pd.read_csv('landslide_data_miss.csv')

def interpolate_missing_values(data):
    for feature in data.columns:
        if data[feature].isnull().any():
            data[feature] = pd.to_numeric(data[feature], errors='coerce')
            for idx in range(len(data)):
                if pd.isnull(data.loc[idx, feature]):
                    previous = data.iloc[:idx][feature].last_valid_index()
                    next_val = data.iloc[idx:][feature].first_valid_index()
                    if previous is not None and next_val is not None:
                        previous_value = data.loc[previous, feature]
                        next_value = data.loc[next_val, feature]
                        data.loc[idx, feature] = previous_value + (next_value - previous_value) * (idx - previous) / (next_val - previous)
    return data

data_interpolated = interpolate_missing_values(data_with_gaps)

def identify_outliers(data):
    outliers = {}
    for feature in data.columns:
        if data[feature].dtype in [float, int]:
            feature_data = data[feature].dropna()
            q1, q3 = feature_data.quantile(0.25), feature_data.quantile(0.75)
            iqr_value = q3 - q1
            lower_bound = q1 - 1.5 * iqr_value
            upper_bound = q3 + 1.5 * iqr_value
            outliers[feature] = feature_data[(feature_data < lower_bound) | (feature_data > upper_bound)].index.tolist()
    return outliers

outliers_data = identify_outliers(data_interpolated)

def compute_median(values):
    values_sorted = sorted(values)
    n = len(values_sorted)
    if n == 0:
        return np.nan
    return values_sorted[n // 2] if n % 2 == 1 else (values_sorted[n // 2 - 1] + values_sorted[n // 2]) / 2

def replace_outliers_with_median(data, outliers):
    for feature, indices in outliers.items():
        if data[feature].dtype in [float, int]:
            median_value = compute_median(data[feature].dropna())
            data.loc[indices, feature] = median_value
    return data

data_no_outliers = replace_outliers_with_median(data_interpolated.copy(), outliers_data)

def normalize_data(data, min_new=5, max_new=12):
    normalized_data = data.copy()
    for feature in data.columns:
        if data[feature].dtype in [float, int]:
            min_old, max_old = data[feature].min(), data[feature].max()
            normalized_data[feature] = min_new + (data[feature] - min_old) * (max_new - min_new) / (max_old - min_old)
    return normalized_data

normalized_data = normalize_data(data_no_outliers)

min_max_before = {col: (data_no_outliers[col].min(), data_no_outliers[col].max()) for col in data_no_outliers.columns if data_no_outliers[col].dtype in [float, int]}
min_max_after = {col: (normalized_data[col].min(), normalized_data[col].max()) for col in data_no_outliers.columns if data_no_outliers[col].dtype in [float, int]}

print("Min and Max values before normalization:")
for feature, (min_val, max_val) in min_max_before.items():
    print(f"{feature}: Min = {min_val}, Max = {max_val}")

print("\nMin and Max values after normalization:")
for feature, (min_val, max_val) in min_max_after.items():
    print(f"{feature}: Min = {min_val}, Max = {max_val}")

def compute_statistics(data):
    means = {}
    std_devs = {}
    for feature in data.columns:
        if data[feature].dtype in [float, int]:
            means[feature] = np.mean(data[feature].dropna())
            std_devs[feature] = np.std(data[feature].dropna(), ddof=0)
    return means, std_devs

means_before, std_devs_before = compute_statistics(data_no_outliers)

def standardize_data(data):
    standardized_data = data.copy()
    for feature in data.columns:
        if data[feature].dtype in [float, int]:
            standardized_data[feature] = (data[feature] - means_before[feature]) / std_devs_before[feature]
    return standardized_data

standardized_data = standardize_data(data_no_outliers)
means_after, std_devs_after = compute_statistics(standardized_data)

print("\nStatistics before standardization:")
for feature in means_before:
    print(f"{feature}: Mean = {means_before[feature]}, Std Dev = {std_devs_before[feature]}")

print("\nStatistics after standardization:")
for feature in means_after:
    print(f"{feature}: Mean = {means_after[feature]}, Std Dev = {std_devs_after[feature]}")
