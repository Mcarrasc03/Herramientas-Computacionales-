import numpy as np
import matplotlib.pyplot as plt
DEuler= np.genfromtxt("DatosEuler.txt", delimiter=", ")
DEulerC= np.genfromtxt("DatosEulerCurioso.txt", delimiter=", ")
DLF= np.genfromtxt("DatosLF.txt", delimiter=", ")
#Euler
time= DEuler[:, 0]
X= DEuler[:, 1]
V= DEuler[:, 2]
X2= DEulerC[:, 1]
#LF
timeLFX=DLF[:, 0]
XLF = DLF[:,1]
timeLFV=DLF[:, 2]
VLF = DLF[:,3]
#Analitica 
w= np.sqrt(50/0.2)
Xreal = np.cos(w*time)
Vreal= -w*np.sin(w*time)

XrealLF = np.cos(w*timeLFX)
VrealLF= -w*np.sin(w*timeLFV)

plt.plot(time, X, label= "Euler")
plt.plot(time, X2, label="Caso curioso de Euler")
plt.title("Comparación Euler", fontsize=16)
plt.xlabel("tiempo", fontsize=14)
plt.legend()
plt.savefig("EulerComp.pdf", format="pdf")
plt.show()

plt.plot(time, X, label= "Posición Euler")
plt.plot(time, V, label="Velocidad Euler")

plt.title("Solución Euler", fontsize=16)
plt.xlabel("tiempo", fontsize=14)
plt.legend()
plt.savefig("Euler.pdf", format="pdf")
plt.show()

plt.plot(timeLFX, XLF, label="Posición")
plt.plot(timeLFV, VLF, label="Velocidad")
plt.title("Solución LeapFrog", fontsize=16)
plt.xlabel("tiempo", fontsize=14)
plt.legend()
plt.savefig("LeapFrog.pdf", format="pdf")
plt.show()