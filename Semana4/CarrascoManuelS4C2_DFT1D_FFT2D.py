import numpy as np
import matplotlib.pylab as plt
import cmath
from scipy.fftpack import fft, fftfreq, fft2, ifft2, fftshift 
from matplotlib.pyplot import imshow, imread
# Construcción de la señal
N = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )
T_k=np.zeros(N, dtype= complex)
n=np.linspace(0,N-1, N, dtype=int)
k_1=np.linspace(0,N-1, N, dtype=int)

for k in range (N):
    T_k[k]=np.sum(y*np.exp(-1j*2*np.pi*k*n/N))
# 1) implemente de la transformada de fourier discreta
T_k=T_k/np.max(T_k)
# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):(bonus)
plt.plot(k_1,T_k)
#plt.xlim(1,-1)
plt.show()
#x_n=np.zeros(N, dtype=complex)
#k=np.linspace(0,N-1, N, dtype=int)
#for n in range (N):
#    x_n[n]=np.sum(y[:N]*np.exp(1j*2*np.pi*n/N)*np.exp(k))
#plt.plot(t, x_n)
#plt.show()
# 3) Haga una gráfica comparando método propio con implementación de scipy.fftpack.fft
fft_x = fft(y) / N # FFT Normalized
freq = fftfreq(N, dt) # Recuperamos las frecuencias
plt.plot(freq, np.abs(T_k))
plt.show()
# 1) Almacene los datos de signal.dat. La columna 1 es el tiempo y la columna 2 es su señal f(t).
#Grafique su señal en función del tiempo.
# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de fourier en función de las frecuencias.

# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. #
#Use la gráfica de la transformada de fourier del punto 3 para determinar un valor apropiado de la frecuencia de corte que debe usar para filtrar dicho ruido de alta frecuencia.

# 4) Grafique la señal filtrada
signal=np.genfromtxt('signal.dat', delimiter=",")
time=signal[:,0]
dt= time[1]-time[0]
señal=signal[:,1]
Nt=len(señal)
nt=np.linspace(0,Nt-1, Nt, dtype=int)
T_t=np.zeros(Nt, dtype= complex)
for z in range (Nt):
    T_t[z]=np.sum(señal*np.exp(-1j*2*np.pi*z*nt/Nt))

#plt.plot(time, signal)
#plt.show()
fft_t=fft(señal)
freqt=fftfreq(Nt, dt)
plt.plot(freqt, np.abs(T_t))
plt.show()
for l in range(Nt):
    frevision=T_t[l]
    if (np.abs(frevision)< 20):
        T_t[l]= 0
    else: 
        continue  
plt.plot(freqt, np.abs(T_t))
plt.show()
t_n=np.zeros(Nt, dtype=complex)
kt=np.linspace(0,Nt-1, Nt, dtype=int)
for h in range (Nt):
    t_n[h]=np.sum(T_t*np.exp(1j*2*np.pi*h*kt/Nt))
plt.plot(time, (t_n))
plt.show()
#__________________________________________________________________________________________________

# 1) Almacene los datos de la imagen (use imread: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html)
Luna = imread("moon.jpg")
# 2) Use la librería de scipy de transformada de fourier en 2d y la trasnformada inversa
#(https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fft2.html)
#para hacer un código que filtre el ruido periodico que tiene la imagen de la luna.
Size=np.shape(Luna)
N=Size[0]
M=Size[1]
Lfrecs = fft2(Luna)
Luna_frec_org= fftshift(Lfrecs)
plt.plot(Lfrecs,Luna_frec_org)
plt.show()
#for i in range(N):
#    for j in range (M):
#        PixelRev= Lfrecs[i, j]
#        if (np.abs(PixelRev)>300000):
#            Lfrecs[i, j] = 0
#        else:
#            continue
for i in range(N):
    for j in range (M):
        PixelRev= Luna_frec_org[i, j]
        if (np.abs(PixelRev)<2000 and np.abs(PixelRev)>1200):
            Lfrecs[i, j] = 0
        else:
            continue
LuNueva=ifft2(Lfrecs)
imshow(np.real(LuNueva))
plt.show()
#3) haga una gráfica de la imagen filtrada y guárdela en LunaFiltrada.png

#imagen: https://blogs.3ds.com/simulia/wp-content/uploads/sites/18/2019/07/NASA_Moon.jpg