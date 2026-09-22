import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fft2, ifft2, fftshift , ifftshift
from matplotlib.pyplot import imshow, imread



# Construcción de la señal
Np = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (Np-1)*dt, Np)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )
T_k=np.zeros(Np, dtype= complex)
n=np.linspace(0,Np-1, Np, dtype=int)
k_1=np.linspace(0,Np-1, Np, dtype=int)
# 1) implemente de la transformada de fourier discreta
def Transformada1(T, fun, en, EN):
    for k in range (EN):
        T[k]=np.sum(fun*np.exp(-1j*2*np.pi*k*en/EN))
    return (T/np.max(T))
def Inversa(T, fun, kn, EN):
    for n in range (EN):
        T[n]=np.sum(fun*np.exp(1j*2*np.pi*kn*n/EN))
    return (T/np.max(T))
# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):
T_k = Transformada1(T_k, y, n, Np)
x_n=np.zeros(Np, dtype=complex)
# 3) Haga una gráfica comparando método propio con implementación de scipy.fftpack.fft
fft_x = fft(y)  
fft_x= fft_x/ np.max(fft_x)# FFT Normalized
freq = fftfreq(Np, dt) # Recuperamos las frecuencias
plt.plot(freq, np.abs(T_k), label= "Implementación propia", linewidth=2)
plt.plot(freq, np.abs(fft_x), label="Funcion de scipy", linewidth=1) #Se cambio el grosor de las lineas para que se pudiera apreciar que estan sobrepuestas 
plt.legend()
plt.show()
print("Ejercicio 1 terminado")
#__________________________________________________________________________________________________________________________
#EJERCICIO 2 
# 1) Almacene los datos de signal.dat. La columna 1 es el tiempo y la columna 2 es su señal f(t).
#Grafique su señal en función del tiempo.
signal=np.genfromtxt('signal.dat', delimiter=",")
time=signal[:,0]
señal=signal[:,1]
dt2= time[1]-time[0]
Nt = len(señal)
St=np.zeros(Nt, dtype= complex)
n2 = np.linspace(0, Nt-1, Nt, dtype=int)

# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de fourier en función de las frecuencias.
St=Transformada1(St, señal, n2, Nt)
freq2=fftfreq(Nt, dt2)
#Gráfica de la Transformada 

fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(10, 5))
axes[0].plot(freq2, np.abs(St))
axes[0].set_title("Espacio de frecuencias")
axes[0].set_xlabel("Frecuencia")
axes[1].set_title("Señal")
axes[1].set_xlabel("tiempo")
axes[1].plot(time, señal)
plt.show()
# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. #
#Use la gráfica de la transformada de fourier del punto 3 para determinar un valor apropiado de la frecuencia de corte que debe usar para filtrar dicho ruido de alta frecuencia.
#Filtro que elimina frecuencias que aportan poco
#for l in range(Nt):
#    frevision=St[l]
#    if (np.abs(frevision)< 0.06):
#        St[l]= 0
#    else: 
#        continue 
#____________________________________________________________________
#Filtro pasa bajos
for l in range(Nt):
    Frecu=freq2[l]
    if (np.abs(Frecu) > 600):
        St[l]= 0
    else: 
        continue  

# 4) Grafique la señal filtrada
t_n=np.zeros(Nt, dtype=complex)
kt=np.linspace(0,Nt-1, Nt, dtype=int)
t_n=Inversa(t_n, St,kt, Nt )
fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(10, 5))
axes[0].plot(freq2, np.abs(St))
axes[0].set_title("Espacio de frecuencias (Filtrada)")
axes[0].set_xlabel("Frecuencia")
axes[1].set_title("Señal (Filtrada)")
axes[1].set_xlabel("tiempo")
axes[1].plot(time, np.real(t_n))
plt.show()
print("Ejercicio 2 terminado")
#__________________________________________________________________________________________________
#EJERCICIO 3
# 1) Almacene los datos de la imagen (use imread: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html)
Luna = plt.imread('moon.jpg')

rows, cols = Luna.shape
# 2) Use la librería de scipy de transformada de fourier en 2d y la trasnformada inversa
#(https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fft2.html)
#para hacer un código que filtre el ruido periodico que tiene la imagen de la luna.
Lfrec = fft2(Luna)
LfrecS = fftshift(Lfrec)

mag = np.abs(LfrecS)
log_mag = np.log(mag + 1e-5) # Magnitud en escala logarítmica


k_size = 17  # Ventana de N x N vecinos 
kernel = np.ones((k_size, k_size)) / (k_size * k_size) #Promedio local de alrededores usando convolución en espectro 

# Alinear el kernel con las dimensiones de la imagen para la convolución FFT
kernel_padded = np.zeros((rows, cols))
kernel_padded[:k_size, :k_size] = kernel
kernel_padded = np.roll(kernel_padded, -k_size // 2, axis=0)
kernel_padded = np.roll(kernel_padded, -k_size // 2, axis=1)
espectro_promedio = ifft2(fft2(log_mag) * fft2(kernel_padded)).real


diferencia = log_mag - espectro_promedio #Comparar cada frecuencia con sus alrededores y detectar anomalías
std_diff = np.std(diferencia)

sensibilidad = 1.8
mascara_ruido = diferencia > (sensibilidad * std_diff)

#No eliminar las bajas frecuencias del centro (Al inicio no se incluyo esto 
#pero la imagen quedaba sin iluminación, esta fue la solución y ahi mejoro la imagen)
cy, cx = rows // 2, cols // 2
radio_centro = 10
y_grid, x_grid = np.ogrid[:rows, :cols]
dist_al_centro = np.sqrt((x_grid - cx)**2 + (y_grid - cy)**2)

mascara_ruido[dist_al_centro <= radio_centro] = False


LfrecS_limpio = LfrecS.copy()
fases = np.angle(LfrecS)
mag_corregida = np.exp(espectro_promedio)

#LfrecS_limpio1[mascara_ruido] = mag_corregida[mascara_ruido] * np.exp(1j * fases[mascara_ruido]) 
#Esta fue en vez de volverla 0 cambiarla a la de los alrededores, pero dio mejor volviendolas 0 
LfrecS_limpio[mascara_ruido] = 0
#3) haga una gráfica de la imagen filtrada y guárdela en LunaFiltrada.png
f_ishift = ifftshift(LfrecS_limpio)
Luna_limpia = np.abs(ifft2(f_ishift))

#Esto fue para compararla original vs nueva #plt.figure(figsize=(14, 5))
                                            #plt.subplot(121)
                                            #plt.imshow(Luna, cmap='gray')
                                            #plt.title('Imagen Original')
                                            #plt.subplot(122)
plt.figure(figsize=(12, 7), dpi=100)
plt.imshow(Luna_limpia, cmap='gray')
plt.axis('off')
plt.savefig("LunaFiltrada.png", format="png", bbox_inches='tight', pad_inches=0, dpi=100)
plt.show()
#imagen: https://blogs.3ds.com/simulia/wp-content/uploads/sites/18/2019/07/NASA_Moon.jpg
print("Ejercicio 3 terminado")
#_______________________________________________________________________________________________________
#Ejercicio 4 
#Recupere la imagen original a partir de la fase y la amplitud de la transformada de fourier (archivos amplitude.dat y phase.dat).
#Recuerde que la transformada de fourier tiene una parte real y una imaginaria
#y recuerde tambien que un numero complejo se puede escribir a partir de la fase y la magnitud que son los datos que usted tiene
#(http://webpages.ursinus.edu/lriley/ref/complex/node1.html)


#1)Descargue los datos de fase y magnitud
amplitud = np.genfromtxt('magnitude.dat')
fase = np.genfromtxt('phase.dat')
#2) construya la transformada de fourier
f_compleja = amplitud * np.exp(1j * fase)


#3) Obtenga la imagen haciendo la transformada inversa
imagen_recuperada = np.abs(ifft2(f_compleja))
plt.imshow(imagen_recuperada, cmap='gray')
plt.title('Imagen Recuperada')
plt.axis('off')
plt.savefig("Reconstrucción.pdf", format="pdf")
plt.show()
print("Ejercicio 4 terminado")