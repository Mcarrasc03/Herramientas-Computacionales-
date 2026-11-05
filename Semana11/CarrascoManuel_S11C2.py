#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

# 1) lea los datos de resorte.dat y almacenelos.
Datos=np.genfromtxt("resorte.dat", delimiter=" ")
t= Datos[:, 0 ]
y_observado= Datos[:, 1 ]
# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por  
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:


# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo  
def mifun(a, gamma, omega):
    return a*np.exp(-gamma*t)*np.cos(omega*t)

# 2b.) Definir una funcion que retorne la funcion de verosimilitud
def verosimilitud(y_obs, y_model):
    chi2=(1/2)*np.sum((y_obs-y_model)**2)
    return np.exp(-chi2)
# 2c.) Caminata

#condiciones iniciales
aini=7.12
gammaini=0.69
omegaini=18.32

#numero de pasos
iteraciones=100000
def algoritmo(ai, gi, oi, N):
    datos_gamma =np.zeros(N, dtype="double")
    datos_a =np.zeros(N, dtype="double")
    datos_omega =np.zeros(N, dtype="double")
    L=np.zeros(N, dtype="double")
    y_modelo= mifun(ai, gi, oi)
    sigmaa = 0.2 
    sigmag = 0.02
    sigmao = 0.5
    for i in range(N):
        g_new=np.random.normal(gi, sigmag)
        a_new=np.random.normal(ai, sigmaa)
        o_new=np.random.normal(oi, sigmao)
        y_modelo_new = mifun(a_new, g_new, o_new) 
        alpha= verosimilitud(y_observado, y_modelo_new)/verosimilitud(y_observado, y_modelo)
        beta=np.random.uniform(0.0, 1.0)
        L[i]=verosimilitud(y_observado, y_modelo_new)
        if (alpha >= 1 ):
            gi=g_new
            datos_gamma[i]=g_new
            ai=a_new
            datos_a[i]=a_new
            oi=o_new
            datos_omega[i]=o_new
        elif(alpha>beta):
            gi=g_new
            datos_gamma[i]=g_new
            ai=a_new
            datos_a[i]=a_new
            oi=o_new
            datos_omega[i]=o_new
        else:
            datos_gamma[i]=gi
            datos_a[i]=ai
            datos_omega[i]=oi
    
    omega_optimo=datos_omega[np.argmax(L)]
    gamma_optimo=datos_gamma[np.argmax(L)]
    a_optimo=datos_a[np.argmax(L)]
    return (a_optimo, gamma_optimo, omega_optimo)


# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."
a_elegido, gamma_elegido, omega_elegido = algoritmo(aini, gammaini, omegaini, iteraciones)
print(f"LOS MEJORES PARAMETROS SON a={a_elegido} gamma={gamma_elegido} Y omgega={omega_elegido}")

def osci(time, a, gamma, omega):
    return a*np.exp(-gamma*time)*np.cos(omega*time)
p0_iniciales = [aini, gammaini, omegaini]
popt, pcov = curve_fit(osci, t, y_observado, p0=p0_iniciales)

print(f"Mejores parámetros encontrados (Hecho por scipy para comparar):a={popt[0]} gamma={popt[1]} Y omgega={popt[2]}")
# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf

plt.scatter(t, y_observado)
y_final = mifun(a_elegido, gamma_elegido, omega_elegido)
plt.plot(t, y_final)
plt.savefig("Resorte.pdf", format="pdf")
plt.close()
# 3) SABIENDO QUE omega=np.sqrt(k/m), IMPRIMA UN MENSAJE DONDE EXPLIQUE SI PUEDE O NO DETERMINAR k Y m DE MANERA INDIVIDUAL USANDO EL METODO ANTERIOR. JUSTIFIQUE BIEN SU RESPUESTA (PUEDE ADEMAS HACER PRUEBAS CON EL CODIGO PARA RESPONDER ESTA PREGUNTA).



