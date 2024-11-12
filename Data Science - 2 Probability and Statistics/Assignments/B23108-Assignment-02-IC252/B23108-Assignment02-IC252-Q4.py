import matplotlib.pyplot as plt
import numpy as np

trials = 10000
x = trials
dice_1 = [1,2,3,4,5,6]
dice_2 = [1,2,3,4,5,6]
y = []
def get_values(x):
    d_1 = np.random.randint(1,7)
    d_2 = np.random.randint(1,7)
    sum = d_1 + d_2
    y.append(sum)
for i in range(1,trials):
    get_values(x)

t = np.arange(2,12+1,1)
k = []
prob_dist = [element/trials for element in k]
for j in t:
    f = (y.count(j))/10000
    k.append(f)
    print(j ,"=", k)

plt.bar(t,k,color=["red","green"])
plt.xlabel("Sum of 2 Dice")
plt.ylabel("Probability Distribution")
plt.show()