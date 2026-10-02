import numpy as np
import matplotlib.pyplot as plt
DEuler= np.genfromtxt("DatosEuler.txt", delimiter=", ")
DLF= np.genfromtxt("DatosLF.txt", delimiter=", ")
DEulerFric= np.genfromtxt("DatosEulerFric.txt", delimiter=", ")
DRK= np.genfromtxt("DatosRK4Fric.txt", delimiter=", ")
#Euler
time= DEuler[:, 0]
X= DEuler[:, 1]
V= DEuler[:, 2]
#LF
timeLFX=DLF[:, 0]
XLF = DLF[:,1]
timeLFV=DLF[:, 2]
VLF = DLF[:,3]
#Analitica 
w= np.sqrt(50/0.2)
Xreal = np.cos(w*time)
Vreal= -w*np.sin(w*time)
#Euler Fricción
XFric= DEulerFric[:, 1]
VFric= DEulerFric[:, 2]
#RK Friccion
XRK=DRK[:,1]
VRK=DRK[:,2]

XrealLF = np.cos(w*timeLFX)
VrealLF= -w*np.sin(w*timeLFV)


plt.plot(time, X, label= "Posición Euler")
plt.plot(time, V, label="Velocidad Euler")
plt.title("Solución Euler", fontsize=16)
plt.xlabel("tiempo", fontsize=14)
plt.legend()
#plt.savefig("Euler.pdf", format="pdf")
plt.show()

plt.plot(timeLFX, XLF, label="Posición")
plt.plot(timeLFV, VLF, label="Velocidad")
plt.title("Solución LeapFrog", fontsize=16)
plt.xlabel("tiempo", fontsize=14)
plt.legend()
#plt.savefig("LeapFrog.pdf", format="pdf")
plt.show()

momentum = 0.2 * V
momentumLF = 0.2 * VLF
plt.plot(XLF, momentumLF, label="Leap Frog")
plt.plot(X, momentum, label="Euler")
plt.title("Espacio de fase", fontsize=16)
plt.xlabel("Posición", fontsize=14)
plt.ylabel("Momento", fontsize=14)
plt.legend()
#plt.savefig("LeapFrog.pdf", format="pdf")
plt.show()

plt.plot(time, XRK, label="Posición")
#plt.plot(time, VRK, label="Euler")
plt.title("RK Fricción", fontsize=16)
plt.xlabel("tiempo", fontsize=14)
plt.ylabel("Posición", fontsize=14)
plt.legend()
#plt.savefig("RKFriccion.pdf", format="pdf")
plt.show()

plt.plot(time, XFric, label="Posición")
#plt.plot(time, VRK, label="Euler")
plt.title("Euler Fricción", fontsize=16)
plt.xlabel("tiempo", fontsize=14)
plt.ylabel("Posición", fontsize=14)
plt.legend()
#plt.savefig("RKFriccion.pdf", format="pdf")
plt.show()