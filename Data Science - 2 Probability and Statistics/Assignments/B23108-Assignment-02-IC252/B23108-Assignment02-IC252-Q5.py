import numpy as np
import matplotlib.pyplot as plt

win_switch=0
win_stick=0

for i in range(10000):
    choices=[0,0,0]
    reward_gate=np.random.randint(1,4)
    choices[reward_gate-1]=1
    door_opened=np.random.randint(1,4)
    
    if(choices[door_opened-1] == 1 and choices[reward_gate - 1] == 1):
        win_stick=win_stick+1
    else:
        win_switch=win_switch+1

prob_stick = win_stick/10000
prob_switch = win_switch/10000
    

xlabels = ["Stick to first choice", "Switching Choice"]
scenario = [prob_stick, prob_switch]

plt.bar(xlabels, scenario, color=["orange", "purple"])
plt.title("Monty Hall Problem")
plt.ylabel("Probability of Winning ")
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()