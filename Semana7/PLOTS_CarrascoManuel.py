import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#DEuler= np.genfromtxt("DatosEulerOr.txt", delimiter=", ")
DLf= np.genfromtxt("DatosLFOr.txt", delimiter=", ")
"""
time= DEuler[:, 0]
X= DEuler[:, 1]
Vx= DEuler[:, 2]
Y= DEuler[:, 3]
Vy= DEuler[:, 4]
"""

timeLFP= DLf[:, 0]
timeLFV= DLf[:, 1]

XLfT= DLf[:, 2]
YLfT= DLf[:, 3]
VxLfT= DLf[:, 4]
VyLfT= DLf[:, 5]

XLfS= DLf[:, 6]
YLfS= DLf[:, 7]
VxLfS= DLf[:, 8]
VyLfS= DLf[:, 9]

fig, ax = plt.subplots(figsize=(6, 6)) 
ax.set_aspect('equal')
ax.plot(XLfT, YLfT, color="blue", label="Orbita Tierra")
ax.set_title("Órbita 2 cuerpos")
ax.set_xlabel("X[UA]")
ax.set_ylabel("Y[UA]")
ax.plot(XLfS, YLfS, color="Yellow", label="Orbita Sol")
ax.legend(loc="upper right")
plt.savefig("Orbita2Cuerpos.pdf", format="pdf")
plt.show()

fig, ax = plt.subplots(figsize=(6, 6)) 
ax.set_aspect('equal')
ax.set_title("Zoom para ver órbita solar")
ax.set_xlabel("X[UA]")
ax.set_ylabel("Y[UA]")
ax.plot(XLfS, YLfS, color="Yellow", label="Orbita Sol")
ax.legend(loc="upper right")
plt.savefig("OrbitaSol.pdf", format="pdf")
plt.show()


