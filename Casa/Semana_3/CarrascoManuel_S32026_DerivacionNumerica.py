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
plt.plot(x,fx, label="cos(x)")
fxplus= np.zeros(M-1)
fxplus= fx[1:M] 
#print(fx) 
#print(fxplus) #Estos dos se usaron para comprobar que si quedaran los indices corridos
dff=((fxplus-fx[:M-1])/h)

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

# 2c). Haga una gráfica de la función y sus derivadas obtenidas usando los dos métodos antes mencionados.
plt.title("Función y su derivada", fontsize=15)
plt.xlabel("X", fontsize=15)
plt.ylabel("f(x)", fontsize=15)
plt.plot(x, dfr, label="-sin(x)")
plt.plot(x[:M-1], dff, label="derivada forward")
plt.plot(x[1:M-1], dfc, label="derivada central")
plt.legend()
plt.show()

# 2d). Haga una grafica con dos subplots (uno por cada metodo) del error |(valor numérico - valor analitico) en el intervalo.

errorf=np.abs(dff-dfr[:M-1])
errorc=np.abs(dfc-dfr[1:M-1])
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].plot(x[:M-1], errorf)
axes[0].set_title(f'Error de derivada forward', fontsize=15)
axes[0].set_xlabel('X', fontsize=15)
axes[0].set_ylabel('Error absoluto', fontsize=15)
axes[1].plot(x[1:M-1], errorc)
axes[1].set_title('Error derivada central', fontsize=15)
axes[1].set_xlabel('X', fontsize=15)
axes[1].set_ylabel('Error Absoluto', fontsize=15)
plt.show()
#Tiene esa forma funcional porque al expandir en Taylor, quedan errores en funcion de derivadas, la diferencia es 
#que el error en de la derivada sentral es de un orden superior a la forward, por eso no son iguales y parecen estar desfasadas 
# 2e). Implemente el algoritmo que le permita calcular la segunda derivada de la función en el intervalo 0 a 2pi. Haga una gráfica de la función y su segunda derivada.
ddf = (fxplus[1:M-1]+fxless[1:M-1]-(2*fx[1:M-1]))/(h*h)
plt.title("Segunda derivada", fontsize=15)
plt.xlabel("X", fontsize=15)
plt.ylabel("f ''(x)", fontsize=15)
plt.plot(x,fx, label="cos(x)")
plt.plot(x[1:M-1], ddf, label="Segunda derivada")
plt.legend(loc='upper right')
plt.show()
#__________________________________________________________________________________________________________________________
# La idea de este ejercicio es que exploren la convergencia del método de Newton-Raphson para encontrar los ceros del siguiente polinomio:

def poli(x):
    	return  (x**5)-(1.7*x**4)-(10.0*x**3)+(20.0*x*x)+ (9.0*x)-18.0
# Para esto:
# 1a.)  Haga una grafica del polinomio en el intervalo [-4:4].
xn=np.linspace(-4,4,M, dtype=float)
fxn=poli(xn)

# 1b.) Usando su implementación de Newton-Raphson, imprima el valor de una raíz x0_r del polinomio encontrada si usa como x_guess inicial el valor -2.35.
#Imprima el valor de x0_r encontrado y de f(x0_r)
def deriv(func, x):
    return (func(x+h)-func(x-h))/(2*h)
x0=-2.35
fx0=poli(x0)
while (np.abs(fx0) >10**-10):
    x0-=(fx0)/ deriv(poli, x0)
    fx0=poli(x0)
plt.title("Polinomio", fontsize=15)
plt.plot(xn, fxn, label="(x^5)-(1.7x^4)-(10x^3)+(20x^2)+ (9x)-18")
plt.xlabel("x", fontsize=15)
plt.ylabel("f(x)", fontsize=15)
plt.scatter(x0, poli(x0), color="red", label=f" x0 = {x0:.4f} empezando en -2.35")
plt.axhline(0, color="black")
plt.legend()
plt.show()
print(x0)
print(poli(x0))
# 1c.) Repita lo anterior para 1000 valores de x_guess generados aleatoriamente en el intervalo [-4:4].
#Cuente cuantas iteraciones necesita su codigo para encontrar una raiz x_r del polinomio (tal que $f(x_r) sea menor a 10^{-10} para cada x_guess.
#Haga una grafica (use un scatter) del numero de iteraciones en funcion del x_guess inicial.
x_guess=np.random.uniform(low=-4,high=4,size=1000)
x_inicial=np.copy(x_guess)#como x_guess se va a ir actualizando hasta llegar a la raiz se crea esta copia
contador_pasos=np.zeros(1000, dtype=int)
for i in range(1000):
  xactual=x_guess[i]
  fxactual=poli(xactual)
  while (np.abs(fxactual) >10**-10):
    xactual-=(fxactual)/ deriv(poli, xactual)
    fxactual=poli(xactual)
    x_guess[i] = xactual 
    contador_pasos[i]+=1
    if (contador_pasos[i]>300): #por si ya gasta muchos pasos que corte en 301, evitando el problema de quedarce en ciclos  
      break
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].set_title("Iteraciones en función de x0i", fontsize=15)
axes[0].set_xlabel("x inicial", fontsize=15)
axes[0].set_ylabel("Numero de iteraciones", fontsize=15)
axes[0].scatter(x_inicial,contador_pasos)
# 1c.) Haga una grafica (use un scatter) de la raíz encontrada (en el eje y) en función del x_guess inicial (en el eje x).
axes[1].scatter(x_inicial,x_guess)
axes[1].set_title("Raiz encontrada en funcion del x0i", fontsize=15)
axes[1].set_xlabel("x inicial", fontsize=15)
axes[1].set_ylabel("Raiz", fontsize=15)
plt.show()
print("Hay un patron interesante comparando las dos gráficas, los valores que necesitan menos iteraciones " \
"solo dan una raiz, mientras que donde se necesitaron muchas, la gráfica de raiz encontrada muestra que" \
" encontro las 3 desde puntos muy cercanos, el problema diria yo, tiene que ver con que en esas zonas " \
"la función tiene una derivada muy chiquita, en la grafica del polinomio se ve que es una sector casi acostado " \
"por lo que los saltos serían grandes y eso proporcionaría mucha variación, además de sumar iteraciones")


