import numpy as np 
import matplotlib.pyplot as plt
Data = np.genfromtxt("Prueba.txt", delimiter=", ")
tiempo=Data[:, 0]
y=Data[:,1]
plt.plot(tiempo,y)
plt.show()