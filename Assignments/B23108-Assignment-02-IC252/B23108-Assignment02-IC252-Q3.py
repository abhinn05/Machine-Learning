import matplotlib.pyplot as plt

def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    
def flip_card(n):
    win = 0
    for i in range(1,n+1):
       win = win + ((-1)**(i+1))/factorial(i) 
    return win

value_n = list(range(2,101))
prob_win = [flip_card(n) for n in value_n]
plt.plot(value_n,prob_win,color="red")
plt.ylabel("Winning Probaility")
plt.xlabel("Value of n")
plt.show()