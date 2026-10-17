import numpy as np
import matplotlib.pyplot as plt
Datos = np.genfromtxt("ExtremosFijos.txt", delimiter=", ")
DatosForzado= np.genfromtxt("ExtremoForzado.txt", delimiter=", ")
x3= Datos[0, :]


for i in range (1000):
    yn=Datos[i+1,:]
    plt.plot(x3, yn)
plt.title("Cuerda con extremos fijos dt=0.5dx/c", fontsize=16)
plt.xlabel("X[m]", fontsize=14)
plt.ylabel("Función u(x,t)[m]", fontsize=14)
plt.savefig("Onda.png", bbox_inches='tight')
plt.close()

for i in range (30):
    yn100=Datos[100*i+1,:]
    plt.plot(x3, yn100)
plt.title("Cuerda con extremos fijos dt=0.5dx/c", fontsize=16)
plt.xlabel("X[m]", fontsize=14)
plt.ylabel("Función u(x,t)[m]", fontsize=14)
plt.savefig("Onda_Cada100.png", bbox_inches='tight')
plt.close()

for i in range (30):
    yf=DatosForzado[100*i+1,:]
    plt.plot(x3, yf)
plt.title(r"Cuerda con extremo forzados w= 100 $\pi$ y A = 0.05", fontsize=16)
plt.xlabel("X[m]", fontsize=14)
plt.ylabel("Función u(x,t)[m]", fontsize=14)
plt.savefig("Onda_Forzada.png", bbox_inches='tight')
plt.close()