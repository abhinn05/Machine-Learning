import numpy as np
import matplotlib.pyplot as plt
def f(x:np.ndarray) -> np.ndarray :
    y = ((np.power(np.sin(x),7))) + ((np.power((np.cos(x)),5))) / np.exp(x)
    return y
steps = 0.1 
x = np.arange(0,4,steps)
y = f(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of f(x)")
plt.show()