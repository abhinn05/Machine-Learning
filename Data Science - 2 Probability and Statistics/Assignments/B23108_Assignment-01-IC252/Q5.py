import numpy as np
import matplotlib.pyplot as plt
x = np.arange((-10*np.pi),(10*np.pi),0.1)
y = np.array(np.sin(x))
plt.subplot(3,1,1)
plt.plot(x,y)
plt.title("SINE Wave")
plt.xlabel("Radians")
plt.ylabel("Sin Value")
plt.legend(["Sin"],loc='right')

t = np.array(np.cos(x))
plt.subplot(3,1,3)
plt.plot(x,y)
plt.title("Cos Wave")
plt.xlabel("Radians")
plt.ylabel("Cos Value")
plt.legend(["Cos"],loc='right')
plt.show()