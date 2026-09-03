import numpy as np
import matplotlib.pylab as plt

# Función a integrar
def funcion(x1):
    	return np.cos(x1)
#El intervalo de integración es de 0 a 3pi/2.
#Divida el intervalo de integración en M secciones para calcular sus integrales.
#pruebe distintos valores de M

# paso 1: use linespace (ver documentación: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
# para hacer el arreglo de su intervalo en x
M=9999
a=0
b=3*np.pi/2
x = np.linspace(a, b, M, dtype = float)
def integral(x):
    return np.sum(x)

#paso 2: genere el arreglo de valores de su función fx:
fx = funcion(x)



# 2a). Usando el método de suma de rectángulos, calcule la integral de la función.
#Compare su valor obtenido numéricamente con el valor analitico e imprima ambos valores.
w=np.zeros(M)
h=(b-a)/(M-1)
w2=h+w
w3=h+w
rec = h*fx


# 2b). Usando el método de trapezoide, calcule la integral de la función.
#Compare su valor obtenido numéricamente con el valor analitico e imprima ambos valores.
area= integral(rec)-(h/2)*funcion(x[0])-(h/2)*funcion(x[M-1])
wt = w2 
wt[0]=(h/2)
wt[M-1]=(h/2)
tra=wt*fx

# 2c). Usando el método de Simpson, calcule la integral de la función.
#Compare su valor obtenido numéricamente con el valor analitico e imprima ambos valores.
ws=w3
print(ws)
ws[0]=h/3
ws[-1]=h/3
ws[1:-2:2]=4*h/3
ws[2:-3:2]=2*h/3
sim=ws*fx
print(f"El resultado por rectangulos es {integral(rec)}")
print(f"El resultado por trapecios es {integral(tra)}")
print(f"El resultado por trapecios es {area} usando otra forma")
print(f"El resultado por simpson es{integral(sim)}")