import numpy as np
import matplotlib.pyplot as plt
Dar= np.genfromtxt("ArregloAleatorio.txt", delimiter=", ")
indice= Dar[:,0]
Valor= Dar[:,1]
plt.scatter(indice, Valor)
plt.title("Números aleatorios entre 0 y 900", fontsize=16)
plt.xlabel("Índice", fontsize=14)
plt.ylabel("Valor aleatorio", fontsize=14)
plt.savefig("aleatorios.png", format="png")
