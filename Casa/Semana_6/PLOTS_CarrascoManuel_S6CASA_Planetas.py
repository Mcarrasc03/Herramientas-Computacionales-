import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

DEuler= np.genfromtxt("DatosEulerOr.txt", delimiter=", ")
DLf= np.genfromtxt("DatosLFOr.txt", delimiter=", ")
time= DEuler[:, 0]
X= DEuler[:, 1]
Vx= DEuler[:, 2]
Y= DEuler[:, 3]
Vy= DEuler[:, 4]


timeLFP= DLf[:, 0]
XLf= DLf[:, 1]
VxLf= DLf[:, 2]
timeLFV= DLf[:, 3]
YLf= DLf[:, 4]
VyLf= DLf[:, 5]

fig, ax = plt.subplots(figsize=(6, 6)) 
ax.set_aspect('equal')

cir= plt.Circle((0, 0), 0.00465, color='yellow', fill=True, alpha=0.9, label="Sol")
ax.add_patch(cir)
ax.plot(X, Y, label = "Euler")
ax.set_title("Orbita de la tierra, problema de 2 cuerpos")
ax.plot(XLf, YLf, label="Leap-Frog")
ax.legend(loc="upper left")
plt.savefig("Orbita.pdf", format="pdf")
plt.show()


