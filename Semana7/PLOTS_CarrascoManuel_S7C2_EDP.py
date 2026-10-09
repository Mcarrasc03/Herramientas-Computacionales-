import numpy as np
import matplotlib.pyplot as plt
dat3 = np.genfromtxt("ExtremosFijos.txt", delimiter=", ")
x3= dat3[0, :]

for i in range (1000):
    yc=dat3[i+1,:]
    plt.plot(x3, yc)
plt.title("Cuerda con extremos fijos", fontsize=16)
plt.xlabel("X", fontsize=14)
plt.ylabel("Función u(x,t)", fontsize=14)
plt.savefig("Onda.png", bbox_inches='tight')

