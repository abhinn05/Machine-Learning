import numpy as np
import matplotlib . pyplot as plt
val = np . random . normal ( size =(100) , scale =3 , loc =10)
hbins =np.arange(0 ,20 ,1)
plt.hist( val , bins =20,color='blue',edgecolor='black')
plt.ylabel("Marks of Class")
plt.xlabel("Class Interval")
plt.hist( val ,bins =hbins,color="orange",edgecolor='black')
plt . show ()