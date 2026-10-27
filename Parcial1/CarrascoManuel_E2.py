print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++  Ejercicio 2: Integración numérica +++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++")

#En este script debe implementar dos métodos de integración (Monte Carlo y Trapezoide) para calcular la integral de la función en el intervalo [-2;2].

import numpy as np
import matplotlib.pylab as plt
def mifun(x):
    y=x*x*3-2
    return y
xfun = np.linspace(-2, 2, 1000)
h=xfun[20]-xfun[19]
yfun=mifun(xfun)
plt.plot(xfun, yfun)
# 1) Use el método de Monte Carlo para calcular la integral.
x=np.random.uniform(-2,2)
y=np.random.uniform(-2,2)
xlimn = -np.sqrt(2/3)
xlimp = np.sqrt(2/3)
contadorp=0
contadorn=0 
N=1000
for i in range (N):
    xran=np.random.uniform(-2,xlimn)
    yran=np.random.uniform(-2,10)
    x=xran
    y=yran 
    if(mifun(x)>y and y >0):
        contadorp+=1
        plt.scatter(x,y, color="green")    
    else:
        plt.scatter(x,y, color="orange") 

for i in range (N):
    xran=np.random.uniform(xlimn,xlimp)
    yran=np.random.uniform(-2,10)
    x=xran
    y=yran 
    if(mifun(x)<y and y < 0):
        contadorn+=1
        plt.scatter(x,y, color="red")    
    else:
        plt.scatter(x,y, color="orange")  

for i in range (N):
    xran=np.random.uniform(xlimp,2)
    yran=np.random.uniform(-2,10)
    x=xran
    y=yran 
    if(mifun(x)>y and y >0):
        contadorp+=1
        plt.scatter(x,y, color="green")    
    else:
        plt.scatter(x,y, color="orange")   
plt.show()
    
Areap= contadorp * (20*(2-xlimp))/ 2*N 
Arean = contadorn * (10*(xlimp-xlimn))/ N     
Area = Areap-Arean   
print(Area)
     
# 2) use el método del trapezoide para calcular la integral.
area= np.sum(yfun*h) - yfun[0]*h/2 -yfun[-1]*h/2
print(area)
# 3) Descomente y complete el siguiente mensaje con sus resultados obtenidos:

#print(f"el resultado de la integral por el método de monte Carlo es:\n{X llene acá el nombre de su variable X}\ny el resultado usando el método del trapezoide es:\n{X llene acá el nombre de su variable X}")

