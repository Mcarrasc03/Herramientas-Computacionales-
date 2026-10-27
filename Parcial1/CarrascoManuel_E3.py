print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++  Ejercicio 3: Geometría +++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")

import numpy as np
import matplotlib.pylab as plt


# A continuación se generan 5 numeros aleatorios c1x, c1y, r, c2x y c2y. 

#1) Encuentre el radio maximo de un círculo cuyo centro tiene coordenadas (c2x,c2y) y está completamente contenido dentro del círculo centrado en (c1x,c1y) y radio r. 

#centro del circulo 
c1x=np.random.uniform(-50, 50)
c1y=np.random.uniform(-50, 50)
print(c1x,c1y)

#radio circulo
r=np.random.uniform(100, 200)
print(r)

#vertice del rectangulo dentro del circulo
c2x=np.random.uniform(c1x+0.2*r, c1x+0.5*r)
c2y=np.random.uniform(c1y+0.2*r, c1y+0.5*r)
print(c2x,c2y)

m=(c2y-c1y)/(c2x-c1x)
def recta(x): 
    y = m*(x-c2x) + c2y
    return y 
xre= np.linspace(c1x, c2x+r, 1000)
yre= recta(xre) 
xcir=np.linspace(c1x, c2x+r, 1000)
ycir = np.sqrt(r*r - (xcir-c1x)*(xcir-c1x)) + c1y
xz=0
rad=0
for i in range (1000):
    if((np.abs(yre[i]-ycir[i]) < 0.001) and (np.abs(xre[i]-xcir[i])< 0.0001)):
        rad = yre[i]
        xz=xre[i]
        break 
    else:
        continue
rmax = np.sqrt((xz-c2x)*(xz-c2x) + (rad-c2y)*(rad-c2y))         

#2) Graficar el círculo y los vértices del cuadrado (ejemplo a continuación) 

#grafica:
figure, axes = plt.subplots()
axes.set_aspect( 1 )
axes.set(xlim=(c1x-1.1*r,c1x+1.1*r), ylim=(c1y-1.1*r,c1y+1.1*r))
plt.scatter(c1x,c1y)
plt.scatter(c2x,c2y)
axes.add_artist(plt.Circle((c1x,c1y),r, fill=False))
#descoemente la siguiente linea con su valor encontrado
axes.add_artist(plt.Circle((c2x,c2y),rmax, fill=False))
plt.show()

