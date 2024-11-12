import pandas as pd
import math

df = pd.read_csv(r"D:\\College\\Sem 3\\Machine Learning\\2024\\Assignments\\Assignment_1\\landslide_data_original.csv")
# print(df)

print("The Statistical Measures of Temperature attributes are : \n")

col_sum = df['temperature'].sum()
row_count = df['temperature'].count()

mean = col_sum/row_count
print("Mean = ",mean)

max_value = float('-inf')
for i in range(len(df['temperature'])):
    value = float(df['temperature'][i])
    if value>max_value:
        max_value = value
print("Max = ",max_value)

min_value = float('inf')
for i in range(len(df['temperature'])):
    value = float(df['temperature'][i])
    if value<min_value:
        min_value = value
print("Min = ",min_value)

column_data = df['temperature'].tolist()

sorted(column_data)
n = len(column_data)
median = 0
if(n%2==0):
    median = (column_data[n//2] + column_data[(n//2) - 1])/2
else:
    median = column_data[n//2]

print("Median = ",median)


def std(mean,data):
    for i in column_data:
        variance = (((i-mean) ** 2).sum()) / n
        std_dev = math.sqrt(variance)
    print("Variance = ",std_dev)
std(mean,column_data)
