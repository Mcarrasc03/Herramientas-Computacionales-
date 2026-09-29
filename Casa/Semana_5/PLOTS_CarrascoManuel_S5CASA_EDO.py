import numpy as np
import matplotlib.pyplot as plt
DEuler= np.genfromtxt("DatosEuler.txt", delimiter=", ")
DRk = np.genfromtxt("DatosRK4.txt", delimiter= ", " )
DErrores= np.genfromtxt("ErroresEDO.txt", delimiter= ", " )
h = DErrores[:,0]
ErrEu=DErrores[:,1]
ErrRK=DErrores[:,2] 
time= DEuler[:, 0]
Eu= DEuler[:, 1]
Rk=DRk[:,1]
ft= np.exp(-1*time)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(h, ErrEu)
axes[0].set_title("Error promedio de Euler", fontsize=16)
axes[0].set_xlabel("Número de puntos", fontsize=14)
axes[1].plot(h[:50], ErrRK[:50])
axes[1].set_title("Error promedio de RK4", fontsize=16)
axes[1].set_xlabel("Número de puntos", fontsize=14)
plt.savefig("Errores.pdf", format="pdf")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
axes[0].plot(time, Eu, label="Solución Euler")
axes[0].plot(time, Rk, label="Solución RK4")
axes[0].plot(time, ft, label="Solución analítica")
axes[0].legend()
axes[0].set_title("Solución a la ecuación diferencial", fontsize=15)
axes[0].set_xlabel("t", fontsize=14)
axes[1].plot(time, Eu, label="Solución Euler")
axes[1].plot(time, Rk, label="Solución RK4")
axes[1].plot(time, ft, label="Solución analítica")
axes[1].set_xlabel("t", fontsize=14)
axes[1].set_xlim(1.0, 1.001)
axes[1].set_ylim(np.exp(-1.001), np.exp(-1))
axes[1].set_title("Zoom para ver la diferencia", fontsize=15)
axes[1].legend()
axes[2].plot(time, Rk, label="Solución RK4", color="orange")
axes[2].plot(time, ft, label="Solución analítica", color= "green")
axes[2].set_xlabel("t", fontsize=14)
axes[2].set_xlim(1.0, 1.000005)
axes[2].set_ylim(np.exp(-1.000005), np.exp(-1))
axes[2].set_title("Más zoom para ver la diferencia", fontsize=15)
axes[2].legend()
plt.savefig("SoluciónEDO.pdf", format="pdf")
