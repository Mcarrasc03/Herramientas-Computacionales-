import numpy as np
import matplotlib.pyplot as plt
dat= np.genfromtxt("Datosini.txt", delimiter=", ")
dat2= np.genfromtxt("Pos.txt", delimiter=", ")
dat3 = np.genfromtxt("pos.txt", delimiter=", ")
x= dat[:, 0]
y=dat[:, 1]

x2= dat2[:, 0]
y2=dat2[:, 1]

x3= dat3[0,:]
y3= dat3[1, :]

x4= dat3[0,:]
y4= dat3[2, :]

x5= dat3[0,:]
y5= dat3[3, :]

x6= dat3[0,:]
y6= dat3[4, :]

x7= dat3[0,:]
y7= dat3[5, :]

x8= dat3[0,:]
y8= dat3[6, :]

x9= dat3[0,:]
y9= dat3[7, :]

x10= dat3[0,:]
y10= dat3[8, :]

x11= dat3[0,:]
y11= dat3[9, :]

plt.plot(x, y)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.plot(x7, y7)
plt.plot(x8, y8)
plt.plot(x9, y9)
plt.plot(x10, y10)
plt.plot(x11, y11)
plt.savefig("Onda.png")
plt.show()