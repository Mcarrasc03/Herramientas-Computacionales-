import numpy as np
import matplotlib.pyplot as plt
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
r = np.sqrt(X*X + Y*Y)
plt.plot(time, X)
plt.plot(time, Y)
plt.show()
plt.plot(X, Y)
plt.plot(XLf, YLf)
plt.scatter(0, 0, color="yellow", s=500)
plt.show()
