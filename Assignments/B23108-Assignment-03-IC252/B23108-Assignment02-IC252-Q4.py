import math
import numpy as np

#a
p = ((math.comb(4,3)*math.comb(13,1)*math.comb(12,1)*math.comb(4,2))/math.comb(52,5))
print("Probability of getting a Full House ",p)

#b
def output():
    x=np.arange(52)
    for i in range(52):
        x[i]=x[i]//4
    np.random.shuffle(x)
    output=x[0:5]
    return output


def house_full(x):
    x.sort()
    if x[0]==x[1]==x[2] and x[3]==x[4] and x[0]!=x[3]:
        return True
    
    elif x[0]==x[1] and x[2]==x[3]==x[4] and x[0]!=x[2]:
        return True
    else:
        return False

sum=0
for i in range(0,1001):
    o=output()
    if house_full(o)==True:
        sum+=1
pb=sum/1000
print("Probability Through Simulation: ",pb)

#c
pf=(1-p)
p0=math.pow(pf,1000)
p1=math.comb(1000,1)*math.pow(pf,999)*p
pc=1-p0-p1
print("Probability of getting atleast 2 Full Houses in 1000 Trials Theoretically: ",pc)


z=0
r=[]
for k in range(1001):
    sum=0
    for j in range(0,1001):
        oc=output()
        if house_full(oc)==True:
            sum+=1
    r.append(sum)
    if sum>=2:
        z+=1

print("Probability of getting atleast 2 full houses in 1000 Trials through Simulation: ",z/1000)
print("Mean: ",np.mean(r))
print("Variance: ", np.var(r))
