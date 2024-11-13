#a
import math
import numpy as np
import matplotlib.pyplot as plt

lambda_val = 57

wait = np.linspace(0, 1, 1000)

pdf = lambda_val * np.exp(-lambda_val * wait)

plt.plot(wait, pdf, label='PDF')
plt.xlabel('Wait time in hours')
plt.ylabel('Probability density')
plt.title('PDF of Wait Time for the Next Covid-19 Confirmed Case')
plt.legend()
plt.show()

#b
lambda_val = 57
def CDF(y):
    a = 1 - np.exp(-lambda_val*y)
    return a
p1 = CDF(1/60)
print("Probability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute",p1)

#c
p2 = CDF(2/60)
print("Probability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes : ",p2-p1)


#d

p3 = 1 - p2
print("Probability of the wait time for the next Covid-19 confirmed case to be more than 2 minutes : ",p3)

#e

lambda_val = 57*2

def CDF2(y):
    a = 1 - np.exp(-lambda_val*y)
    return a
p5 = CDF2(2/60)
p4 = CDF2(1/60)
print("Probability of wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes : ",p5-p4)