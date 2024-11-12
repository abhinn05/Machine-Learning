import numpy as np
import matplotlib.pyplot as plt
from statistics import NormalDist as nd

mean=150
standard_dev=10
count=0
dist=nd(150,10)
samples = np.random.normal(mean, standard_dev, 100)
print(samples)
for i in range(len(samples)):
    if samples[i]<140:
        count+=1
        
prob1=count/100
print("The probability that a randomly selected widget weighs less than 140 grams is",prob1)
print("Therotical value: ",dist.cdf(140))

samples.sort()
top_5_percent_cutoff = np.percentile(samples, 95)

print("Minimum weight for premium products:", top_5_percent_cutoff, "grams")

max_nondefective= np.percentile(np.random.normal(mean, standard_dev, 10000), 10)
print("The maximum weight allowed for a widget to be considered within the acceptable range is",max_nondefective)

cases=100-10-5
print("The probability that a product is neither premium nor defective is",cases/100)