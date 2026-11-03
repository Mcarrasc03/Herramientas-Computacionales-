# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion.
def mifun(x):
	x_0 = 3.0
	a = 0.01
	return np.exp(-(x**2))/((x-x_0)**2 + a**2)

# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y pasos son los parametros que recibe la funcion.
x_fun =np.linspace(-4,4,1000)
y_fun =mifun(x_fun)
area= np.trapezoid(y_fun, x_fun, dx=0.001)
print(area)

def algoritmo(sig, N, func):
    x_inicial=np.random.uniform(-4, 4)
    x_guardados=np.array([])
    for i in range(N):
        x_new=np.random.normal(x_inicial, sig)
        alpha=func(x_new)/func(x_inicial)
        beta=np.random.uniform(0.0, 1.0)
        if (alpha >= 1 ):
            x_guardados=np.append(x_guardados, x_new)
            x_inicial=x_new
            #x_guardados[i]=x_inicial 
        elif(alpha>beta):
            x_inicial=x_new
            x_guardados=np.append(x_guardados, x_new)
            #x_guardados[i]=x_inicial 
        else:
            x_guardados=np.append(x_guardados, x_inicial)
            
    return x_guardados

x_save=algoritmo(0.2, 100000, mifun)

plt.hist(x_save, bins= 100, range=(-4,4), density= True)
plt.plot(x_fun, y_fun/area)
plt.savefig("histograma_0.2_100000.pdf")
        
# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000
# sigma = 0.2, pasos =100000
# sigma = 0.01, pasos =100000
# sigma = 0.1, pasos =1000
# sigma = 0.1, pasos =100000
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.