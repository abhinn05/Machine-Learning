import pandas as pd
import math

def mean(data):
    return sum(data) / len(data)

def covariance(x, y, x_mean, y_mean):
    return sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x))) / len(x)

def standard_deviation(data, mean_value):
    return math.sqrt(sum((x - mean_value) ** 2 for x in data) / len(data))

def pearson_correlation(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    cov = covariance(x, y, x_mean, y_mean)
    std_x = standard_deviation(x, x_mean)
    std_y = standard_deviation(y, y_mean)
    return cov / (std_x * std_y)

df = pd.read_csv("D:\\College\\Sem 3\\Machine Learning\\2024\\Assignments\\Assignment_1\\landslide_data_original.csv")

x = df['lightavg'].dropna()  
y = df['temperature'].dropna()  

correlation = pearson_correlation(x, y)

print("Pearson Correlation Coefficient:", correlation)
