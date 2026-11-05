print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++  Ejercicio 1: Derivación numérica +++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")

#En el archivo XXXX.dat, están los datos de posición en función del tiempo de un proyectil.

import numpy as np
import matplotlib.pylab as plt
datos=np.genfromtxt("E1_datos.dat", delimiter= " ", comments="#")
tiempo=datos[:,0]
posicion=datos[:, 1]
dt= tiempo[1]-tiempo[0]
# 1) Haga una gráfica de posicion en función del tiempo.
plt.plot(tiempo, posicion)
plt.title("Posición en función del tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
plt.show()
# 2) Usando el algoritmo de central difference, calcule la derivada de los datos de posición y haga una gráfica de velocidad (que es la derivada de la posición) en función del tiempo.
posicion_siguiente= np.copy(posicion[1:])
posicion_anterior=np.zeros(len(posicion)-1, dtype="double")
posicion_anterior[1:]= np.copy(posicion[:-2])

print(posicion_anterior[92:])
print(posicion[92:])                #Para ver el cambio de los indices y comparar si es correcto
print(posicion_siguiente[92:])

print(len(posicion_anterior))
print(len(posicion))                #Deberia ser diferencia de -2, para no complicarme la diferencia es de -1 pero el primer
print(len(posicion_siguiente))      #incide no se usa, ninguna de las esquinas tiene derivada por no conocer el antes ni el despues de estos. 

derivada= (posicion_siguiente[1:]-posicion_anterior[1:])/(2*dt)
plt.plot(tiempo[1:-1], derivada)
plt.title("Posición en función del tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.show()