import matplotlib.pyplot as plt
import numpy as np

Datos = np.genfromtxt("Datos_LF_PLANETAS.txt", delimiter=", ")

x_tierra = Datos[:, 2]
y_tierra = Datos[:, 3]
x_sol = Datos[:, 6]
y_sol = Datos[:, 7]

plt.plot(x_tierra, y_tierra, color="navy", label= "Tierra")
plt.plot(x_sol, y_sol, color="yellow", label="Sol")
plt.title("Órbitas 2 cuerpos", fontsize=14)
plt.xlabel("X [UA]", fontsize=12)
plt.ylabel("Y [UA]", fontsize=12)
plt.legend()
plt.savefig("Orbitas.png")
plt.close()
plt.plot(x_sol, y_sol, color="yellow", label="Sol")
plt.title("Órbita Sol", fontsize=14)
plt.xlabel("X [UA]", fontsize=12)
plt.ylabel("Y [UA]", fontsize=12)
plt.legend()
plt.savefig("OrbitaSol.png")
plt.close()