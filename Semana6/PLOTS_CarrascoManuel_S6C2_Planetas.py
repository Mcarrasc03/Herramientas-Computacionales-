import numpy as np
import matplotlib.pyplot as plt
DEuler= np.genfromtxt("DatosEulerOr.txt", delimiter=", ")
time= DEuler[:, 0]
X= DEuler[:, 1]
Vx= DEuler[:, 2]
Y= DEuler[:, 3]
Vy= DEuler[:, 4]
r = np.sqrt(X*X + Y*Y)
plt.plot(time, X)
plt.plot(time, Y)
plt.show()
plt.plot(X, Y)
plt.show()