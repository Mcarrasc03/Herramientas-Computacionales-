#Este ejercicio busca que usted implemente correctamente dos métodos de derivación numérica: forward difference y central difference.
#Pruebe distintos valores de h (que equivale a distintos valores de M).

import numpy as np
import matplotlib.pyplot as plt

# Función a derivar
def funcion(x1):
    	return np.cos(x1)
#El intervalo de integración es de 0 a 2pi.
#Divida el intervalo de integración en M secciones para calcular sus derivadas.
#pruebe distintos valores de M

# paso 1: use linespace (ver documentación: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
# para hacer el arreglo de su intervalo en x
M=9999
a=0
b=2.0*np.pi
h=(b-a)/(M-1)
#1) grafique su función para verificar que hizo bien los pasos anteriores
x = np.linspace(a, b, M, dtype = float)

# 2a). Implemente el algoritmo que le permita calcular la derivada de la función para los puntos en el intervalo 0 a 2pi usando forward difference.

fx = funcion(x)
dfr=-1*np.sin(x)
plt.plot(x,fx)
fxplus= np.zeros(M-1)
fxplus= fx[1:M] 
#print(fx) 
#print(fxplus) #Estos dos se usaron para comprobar que si quedaran los indices corridos
dff=((fxplus-fx[:M-1])/h)
#plt.plot(x[:M-1], dff)
#plt.show()
# 2b). Implemente el algoritmo que le permita calcular la derivada de la función para los puntos en el intervalo 0 a 2pi usando diferencia central.
fxless=np.zeros(M-1)
fxless[1:M-1]= fx[:M-2]
#print(fxless)
#print(fx) 
#print(fxplus)
#print(np.shape(fxless))
#print(np.shape(fx))
#print(np.shape(fxplus)) #Estos 6 valores se usaron para comprobar que si quedaran los indices corridos y los tamaños de los arreglos 
dfc=(fxplus[1:M-1]-fxless[1:M-1])/(2*h)
#plt.plot(x[1:M-1], dfc)
#plt.show()
# 2c). Haga una gráfica de la función y sus derivadas obtenidas usando los dos métodos antes mencionados.
plt.plot(x[:M-1], dff)
plt.plot(x[1:M-1], dfc)
plt.plot(x, dfr)
plt.show()

# 2d). Haga una grafica con dos subplots (uno por cada metodo) del error |(valor numérico - valor analitico) en el intervalo.

errorf=np.abs(dff-dfr[:M-1])
errorc=np.abs(dfc-dfr[1:M-1])
plt.plot(x[:M-1], errorf)
plt.show()
plt.plot(x[1:M-1], errorc)
plt.show()

# 2e). Implemente el algoritmo que le permita calcular la segunda derivada de la función en el intervalo 0 a 2pi. Haga una gráfica de la función y su segunda derivada.
ddf = (fxplus[1:M-1]+fxless[1:M-1]-(2*fx[1:M-1]))/(h*h)
plt.plot(x[1:M-1], ddf)
plt.show()
#__________________________________________________________________________________________________________________________
# La idea de este ejercicio es que exploren la convergencia del método de Newton-Raphson para encontrar los ceros del siguiente polinomio:

def poli(x):
    	return  (x**5)-(1.7*x**4)-(10.0*x**3)+(20.0*x*x)+ (9.0*x)-18.0
# Para esto:
# 1a.)  Haga una grafica del polinomio en el intervalo [-4:4].
xn=np.linspace(-4,4,M, dtype=float)
fxn=poli(xn)
plt.plot(xn, fxn)
plt.show()
# 1b.) Usando su implementación de Newton-Raphson, imprima el valor de una raíz x0_r del polinomio encontrada si usa como x_guess inicial el valor -2.35.
#Imprima el valor de x0_r encontrado y de f(x0_r)
def deriv(func, x):
    return (func(x+h)-func(x-h))/(2*h)
x0=-2.35
fx0=poli(x0)
while (np.abs(fx0) >0.00000000000000000000000000000000000000000001):
    x0-=(fx0)/ deriv(poli, x0)
    fx0=poli(x0)

print(x0)
print(poli(x0))